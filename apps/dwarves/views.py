from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import render
from django.db import transaction

from apps.dwarves.models import Dwarf
from apps.dwarves.forms import CreateWarband


@login_required(login_url='/mountain', redirect_field_name=None)
def barracks(request):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)

    if request.method == 'POST':
        create_warband = CreateWarband(request.POST)
        if create_warband.is_valid() and not warband.exists():
            dwarf1_name = create_warband.cleaned_data['dwarf1_name']
            dwarf1_quirk = create_warband.cleaned_data['dwarf1_quirk']

            dwarf2_name = create_warband.cleaned_data['dwarf2_name']
            dwarf2_quirk = create_warband.cleaned_data['dwarf2_quirk']

            dwarf3_name = create_warband.cleaned_data['dwarf3_name']
            dwarf3_quirk = create_warband.cleaned_data['dwarf3_quirk']

            dwarf4_name = create_warband.cleaned_data['dwarf4_name']
            dwarf4_quirk = create_warband.cleaned_data['dwarf4_quirk']

            dwarf5_name = create_warband.cleaned_data['dwarf5_name']
            dwarf5_quirk = create_warband.cleaned_data['dwarf5_quirk']

            leader = request.user

            Dwarf.objects.bulk_create([
                Dwarf(name=dwarf1_name, leader=leader),
                Dwarf(name=dwarf2_name, leader=leader),
                Dwarf(name=dwarf3_name, leader=leader),
                Dwarf(name=dwarf4_name, leader=leader),
                Dwarf(name=dwarf5_name, leader=leader)
            ])
    else:
        create_warband = CreateWarband()

    return render(request, "dwarves/barracks.html", {
        'warband': warband,
        'create_warband': create_warband
    })


@login_required(login_url='/mountain', redirect_field_name=None)
def details(request):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)

    return render(request, "dwarves/details.html", {
        'warband': warband
    })
