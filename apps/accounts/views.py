from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.accounts.models import Account
from apps.dwarves.models import Dwarf


@login_required(login_url='/mountain', redirect_field_name=None)
def settings(request):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)

    return render(request, "settings/settings.html", {'warband': warband})


@login_required(login_url='/mountain', redirect_field_name=None)
def profile(request, id):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)

    profile = Account.objects.values('username', 'avatar', 'level', 'profile_text', 'gold', 'rubies').filter(id=id)

    profile_warband = Dwarf.objects.values('name', 'battle_power', 'battles_fought').filter(leader=id)

    return render(request, "profile/profile.html", {
        'warband': warband,
        'profile': profile,
        'profile_warband': profile_warband
    })
