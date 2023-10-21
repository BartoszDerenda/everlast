from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import render
from django.db import transaction

from apps.dwarves.models import Dwarf
from apps.dwarves.forms import CreateWarbandForm


@login_required(login_url='/mountain', redirect_field_name=None)
def barracks(request):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)
    context = {'warband': warband}

    WarbandFormSet = formset_factory(CreateWarbandForm, extra=5, max_num=5,
                                     absolute_max=5, validate_max=5, validate_min=5)

    if request.method == 'POST':
        formset = WarbandFormSet(request.POST)
        if not formset.is_valid():
            print('x')
        if formset.is_valid() and not warband.exists():
            with transaction.atomic():
                for dwarf in formset:
                    name = dwarf.cleaned_data['name']
                    leader = request.user
                    dwarf = Dwarf.objects.create(name=name, leader=leader)
                    dwarf.save()
    else:
        formset = WarbandFormSet()

    context.update({'formset': formset})

    return render(request, "dwarves/barracks.html", context)


@login_required(login_url='/mountain', redirect_field_name=None)
def details(request):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)
    context = {'warband': warband}

    return render(request, "dwarves/details.html", context)
