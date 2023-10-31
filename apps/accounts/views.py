from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render

from .models import Account, Comment, Guestbook
from .forms import CreateComment
from apps.dwarves.models import Dwarf


@login_required(login_url='/mountain', redirect_field_name=None)
def settings(request):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)

    return render(request, "settings/settings.html", {'warband': warband})


@login_required(login_url='/mountain', redirect_field_name=None)
def profile(request, profile_id):
    # Raw variables
    warband = Dwarf.objects.filter(leader=request.user).values('id', 'name', 'status')
    profile_warband = Dwarf.objects.filter(leader=profile_id).values('id', 'name', 'battle_power', 'battles_fought')
    profile_info = Account.objects.filter(id=profile_id).values('username', 'avatar', 'level',
                                                                'profile_text', 'gold', 'rubies',
                                                                'reputation')

    # Converting timestamps into time passed.
    # I know this doesn't look good, pls no bully
    guestbook = Guestbook.objects.all().filter(profile=profile_id).order_by('-id')  # Reverse chronological order
    for guest in guestbook:
        now = timezone.now()
        delta = now - guest.timestamp
        delta = int(delta.total_seconds())

        if delta < 2:
            affix = 'second ago.'
        elif delta in range(2, 59):
            affix = 'seconds ago.'
        elif delta in range(60, 119):
            delta = delta / 60
            affix = 'minute ago.'
        elif delta in range(120, 3599):
            delta = delta / 60
            affix = 'minutes ago.'
        elif delta in range(3600, 7199):
            delta = delta / 3600
            affix = 'hour ago.'
        elif delta in range(7200, 86399):
            delta = delta / 3600
            affix = 'hours ago.'
        elif delta in range(86400, 172799):
            delta = delta / 86400
            affix = 'day ago.'
        else:
            delta = delta / 86400
            affix = 'days ago.'

        guest.timestamp = str(int(delta)) + ' ' + affix

    # Variables for functions
    comment_form = CreateComment()
    author = request.user
    receiver = Account.objects.get(id=profile_id)
    comment_exists = Comment.objects.filter(author=author, receiver=receiver).exists()

    total_battle_power = 0
    for dwarf in profile_warband:
        total_battle_power += dwarf['battle_power']

    # Functions
    def create_comment(author, receiver):
        text = comment_form.cleaned_data['text']
        points = comment_form.cleaned_data['points']
        Account.objects.filter(id=receiver.id).update(reputation=F('reputation') + points)
        comment = Comment.objects.create(author=author, receiver=receiver, text=text, points=points)
        comment.save()

    def delete_comment(author, receiver):
        points = Comment.objects.filter(author=author, receiver=receiver).values('points')
        Account.objects.filter(id=receiver.id).update(reputation=F('reputation') - points)
        Comment.objects.filter(author=author, receiver=receiver).delete()

    if request.method == 'POST':
        if 'create_comment' in request.POST:
            comment_form = CreateComment(request.POST)
            if comment_form.is_valid() and author != receiver:
                if comment_exists:
                    delete_comment(author, receiver)
                create_comment(author, receiver)

        if 'delete_comment' in request.POST:
            delete_comment(author, receiver)

    # After POST so that the comment is visible on first refresh.
    comments = Comment.objects.filter(receiver=profile_id).all()
    your_comment = Comment.objects.filter(receiver=receiver, author=request.user).all()

    # Save visit, delete oldest if above limit
    if author != receiver:
        if Guestbook.objects.filter(profile=receiver, guest=author).exists():
            Guestbook.objects.filter(profile=receiver, guest=author).delete()
        Guestbook.objects.create(profile=receiver, guest=author)
    if Guestbook.objects.filter(profile=receiver).count() >= 5:
        Guestbook.objects.filter(profile=receiver).order_by('timestamp').first().delete()

    # Add redirect with context (impossible?) when user tries to search with URL for a user with ID that does not exist.

    return render(request, "profile/profile.html", {
        'warband': warband,
        'profile_info': profile_info,
        'profile_warband': profile_warband,
        'total_battle_power': total_battle_power,
        'guestbook': guestbook,
        'comments': comments,
        'comment_form': comment_form,
        'your_comment': your_comment
    })
