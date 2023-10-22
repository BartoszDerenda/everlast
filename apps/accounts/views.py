from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Account
from .forms import CreateComment
from apps.dwarves.models import Dwarf


@login_required(login_url='/mountain', redirect_field_name=None)
def settings(request):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)

    return render(request, "settings/settings.html", {'warband': warband})


@login_required(login_url='/mountain', redirect_field_name=None)
def profile(request, user_id):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)
    total_battle_power = 0
    comments = {}

    profile_info = Account.objects.values('username', 'avatar', 'level',
                                          'profile_text', 'gold', 'rubies',
                                          'last_visited', 'comments').filter(id=user_id)

    profile_warband = Dwarf.objects.values('name', 'battle_power', 'battles_fought').filter(leader=user_id)

    for dwarf in profile_warband:
        total_battle_power += dwarf['battle_power']

    for comment in profile_info:
        comments.update(comment['comments'])
        for author_id, text in comment['comments'].items():
            # Potentially super unoptimised - one query per comment on profile? Yikes.
            author = Account.objects.values('username').get(id=author_id)
            comments.update({author_id: [author['username'], text]})

    if request.method == 'POST':
        create_comment = CreateComment(request.POST)
        if create_comment.is_valid():
            text = create_comment.cleaned_data['text']
            author = request.user.id
            Account.objects.update(comments={author: text})
    else:
        create_comment = CreateComment()

    # Add redirect with context (impossible?) when user tries to search with URL for a user with ID that does not exist.

    return render(request, "profile/profile.html", {
        'warband': warband,
        'profile_info': profile_info,
        'profile_warband': profile_warband,
        'total_battle_power': total_battle_power,
        'comments': comments,
        'create_comment': create_comment
    })
