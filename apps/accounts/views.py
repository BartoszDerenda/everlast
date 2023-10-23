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
def profile(request, user_id):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)
    profile_warband = Dwarf.objects.values('name', 'battle_power', 'battles_fought').filter(leader=user_id)
    profile_info = Account.objects.values('username', 'avatar', 'level',
                                          'profile_text', 'gold', 'rubies',
                                          'last_visited').filter(id=user_id)
    total_battle_power = 0
    for dwarf in profile_warband:
        total_battle_power += dwarf['battle_power']

    if request.method == 'POST':
        create_comment = CreateComment(request.POST)
        if create_comment.is_valid():
            text = create_comment.cleaned_data['text']
            points = create_comment.cleaned_data['points']
            Account.objects.update(reputation=F('reputation') + points)
            author = request.user
            comment = Comment.objects.create(author=author, text=text, points=points)
            comment.save()
    else:
        create_comment = CreateComment()

    # After POST so that the comment is visible on first refresh.
    comments = Comment.objects.all().filter(author=user_id)

    # Add redirect with context (impossible?) when user tries to search with URL for a user with ID that does not exist.

    return render(request, "profile/profile.html", {
        'warband': warband,
        'profile_info': profile_info,
        'profile_warband': profile_warband,
        'total_battle_power': total_battle_power,
        'comments': comments,
        'create_comment': create_comment
    })
