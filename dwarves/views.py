from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.db import transaction

from dwarves.forms import CreateWarbandForm
from dwarves.models import Dwarf


@login_required(login_url='/barracks', redirect_field_name=None)
def barracks(request):
    if request.method == 'POST':
        form = CreateWarbandForm(request.POST)
        if form.is_valid():

            with transaction.atomic():
                dwarf_name1 = form.cleaned_data['dwarf_name1']
                leader = request.user
                dwarf1 = Dwarf.objects.create(name=dwarf_name1, leader=leader)
                dwarf1.save()

                dwarf_name2 = form.cleaned_data['dwarf_name2']
                leader = request.user
                dwarf2 = Dwarf.objects.create(name=dwarf_name2, leader=leader)
                dwarf2.save()

                dwarf_name3 = form.cleaned_data['dwarf_name3']
                leader = request.user
                dwarf3 = Dwarf.objects.create(name=dwarf_name3, leader=leader)
                dwarf3.save()

    form = CreateWarbandForm()
    return render(request, "dwarves/barracks.html", {'form': form})
