from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render

from apps.dwarves.models import Dwarf
from apps.dwarves.forms import CreateWarband


@login_required(login_url='/mountain', redirect_field_name=None)
def barracks(request):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)

    if request.method == 'POST':
        create_warband = CreateWarband(request.POST)
        if create_warband.is_valid() and not warband.exists():
            dwarf1_name = create_warband.cleaned_data['dwarf1_name']
            dwarf1_quirk1 = create_warband.cleaned_data['dwarf1_quirk1']
            dwarf1_quirk2 = create_warband.cleaned_data['dwarf1_quirk2']

            dwarf2_name = create_warband.cleaned_data['dwarf2_name']
            dwarf2_quirk1 = create_warband.cleaned_data['dwarf2_quirk1']
            dwarf2_quirk2 = create_warband.cleaned_data['dwarf2_quirk2']

            dwarf3_name = create_warband.cleaned_data['dwarf3_name']
            dwarf3_quirk1 = create_warband.cleaned_data['dwarf3_quirk1']
            dwarf3_quirk2 = create_warband.cleaned_data['dwarf3_quirk2']

            dwarf4_name = create_warband.cleaned_data['dwarf4_name']
            dwarf4_quirk1 = create_warband.cleaned_data['dwarf4_quirk1']
            dwarf4_quirk2 = create_warband.cleaned_data['dwarf4_quirk2']

            dwarf5_name = create_warband.cleaned_data['dwarf5_name']
            dwarf5_quirk1 = create_warband.cleaned_data['dwarf5_quirk1']
            dwarf5_quirk2 = create_warband.cleaned_data['dwarf5_quirk2']

            leader = request.user
            dwarf_names = [dwarf1_name, dwarf2_name, dwarf3_name, dwarf4_name, dwarf5_name]
            dwarf_quirks = [(dwarf1_quirk1, dwarf1_quirk2), (dwarf2_quirk1, dwarf2_quirk2), (dwarf3_quirk1,
                                                                                             dwarf3_quirk2),
                            (dwarf4_quirk1, dwarf4_quirk2), (dwarf5_quirk1, dwarf5_quirk2)]

            new_warband = Dwarf.objects.bulk_create([
                Dwarf(name=dwarf1_name, leader=leader),
                Dwarf(name=dwarf2_name, leader=leader),
                Dwarf(name=dwarf3_name, leader=leader),
                Dwarf(name=dwarf4_name, leader=leader),
                Dwarf(name=dwarf5_name, leader=leader)
            ])

            # Based on their little backstory, it updates the initial attributes of each dwarf.
            for dwarf, (name, quirks) in enumerate(zip(dwarf_names, dwarf_quirks)):
                for quirk in quirks:
                    if quirk == 'Strong':
                        Dwarf.objects.filter(id=new_warband[dwarf].id).update(strength_base=F('strength_base') + 5,
                                                                              endurance_base=F('endurance_base') + 5,
                                                                              speed_base=F('speed_base') - 3)
                    elif quirk == 'Wise':
                        Dwarf.objects.filter(id=new_warband[dwarf].id).update(
                            intelligence_base=F('intelligence_base') + 5,
                            willpower_base=F('willpower_base') + 7,
                            endurance_base=F('endurance_base') - 3)
                    elif quirk == 'Agile':
                        Dwarf.objects.filter(id=new_warband[dwarf].id).update(speed_base=F('speed_base') + 5,
                                                                              agility_base=F('agility_base') + 7,
                                                                              strength_base=F('strength_base') - 3)

                    elif quirk == 'Lucky':
                        Dwarf.objects.filter(id=new_warband[dwarf].id).update(speed_base=F('luck_base') + 7,
                                                                              agility_base=F('charisma_base') + 7,
                                                                              strength_base=F('intelligence_base') - 3)

                    elif quirk == 'Hefty':
                        Dwarf.objects.filter(id=new_warband[dwarf].id).update(intelligence_base=F('endurance_base') + 8,
                                                                              willpower_base=F('strength_base') + 3,
                                                                              endurance_base=F('speed_base') - 3)
    else:
        create_warband = CreateWarband()

    return render(request, "dwarves/barracks.html", {
        'warband': warband,
        'create_warband': create_warband
    })


@login_required(login_url='/mountain', redirect_field_name=None)
def dwarf(request, dwarf_id):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)
    dwarf = Dwarf.objects.all().filter(id=dwarf_id)

    return render(request, "dwarves/dwarf.html", {
        'warband': warband,
        'dwarf': dwarf
    })
