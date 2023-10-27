from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render

from .models import Account, Comment
from .forms import CreateComment
from apps.dwarves.models import Dwarf


@login_required(login_url='/mountain', redirect_field_name=None)
def settings(request):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)

    return render(request, "settings/settings.html", {'warband': warband})


@login_required(login_url='/mountain', redirect_field_name=None)
def profile(request, profile_id):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)
    profile_warband = Dwarf.objects.values('name', 'battle_power', 'battles_fought').filter(leader=profile_id)
    profile_info = Account.objects.values('username', 'avatar', 'level',
                                          'profile_text', 'gold', 'rubies',
                                          'reputation', 'last_visited').filter(id=profile_id)
    total_battle_power = 0
    for dwarf in profile_warband:
        total_battle_power += dwarf['battle_power']

    comment_form = CreateComment()
    author = request.user
    receiver = Account.objects.get(id=profile_id)
    comment_exists = Comment.objects.filter(author=author, receiver=receiver).exists()

    def create_comment(author, receiver):
        text = comment_form.cleaned_data['text']
        points = comment_form.cleaned_data['points']
        Account.objects.filter(id=receiver.id).update(reputation=F('reputation') + points)
        comment = Comment.objects.create(author=author, receiver=receiver, text=text, points=points)
        comment.save()

    def delete_comment(author, receiver):
        points = Comment.objects.values('points').filter(author=author, receiver=receiver)
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
    comments = Comment.objects.all().filter(receiver=profile_id)
    your_comment = Comment.objects.all().filter(receiver=receiver, author=request.user)

    # Add redirect with context (impossible?) when user tries to search with URL for a user with ID that does not exist.

    return render(request, "profile/profile.html", {
        'warband': warband,
        'profile_info': profile_info,
        'profile_warband': profile_warband,
        'total_battle_power': total_battle_power,
        'comments': comments,
        'comment_form': comment_form,
        'your_comment': your_comment
    })
