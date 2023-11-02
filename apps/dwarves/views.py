from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import F
from django.shortcuts import render

from apps.dwarves.models import Dwarf
from apps.dwarves.forms import CreateWarband
from apps.items.models import Armor


@login_required(login_url='/mountain', redirect_field_name=None)
def barracks(request):
    warband = Dwarf.objects.filter(leader=request.user).values('id', 'name', 'status')

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
    warband = Dwarf.objects.filter(leader=request.user).values('id', 'name', 'status')
    dwarf_info = Dwarf.objects.filter(id=dwarf_id).values()

    def unpacking_equipment(query):
        for item in query:
            for slot, name in item.items():
                if name is None:
                    return False
                return name

    # Equipment
    equipped_items = Dwarf.objects.filter(id=dwarf_id).values('head', 'shoulders', 'chest', 'gloves',
                                                              'pants', 'boots', 'trinket')
    equipment = {}
    for eq_piece in equipped_items:
        for slot, item_name in eq_piece.items():
            if Armor.objects.filter(name=item_name).exists():
                equipment.update({slot: Armor.objects.get(name=item_name)})
            else:
                equipment.update({slot: "No armor."})

    # Updating attributes
    dwarf_attr = {}
    for d in dwarf_info:
        dwarf_attr.update(
            {'strength_total': int(d['strength_base'] * d['strength_multiplier'] + d['strength_bonus'])})
        dwarf_attr.update(
            {'intelligence_total': int(
                d['intelligence_base'] * d['intelligence_multiplier'] + d['intelligence_bonus'])})
        dwarf_attr.update(
            {'endurance_total': int(d['endurance_base'] * d['endurance_multiplier'] + d['endurance_bonus'])})
        dwarf_attr.update(
            {'speed_total': int(d['speed_base'] * d['speed_multiplier'] + d['speed_bonus'])})
        dwarf_attr.update(
            {'agility_total': int(d['agility_base'] * d['agility_multiplier'] + d['agility_bonus'])})
        dwarf_attr.update(
            {'willpower_total': int(d['willpower_base'] * d['willpower_multiplier'] + d['willpower_bonus'])})
        dwarf_attr.update(
            {'charisma_total': int(d['charisma_base'] * d['charisma_multiplier'] + d['charisma_bonus'])})
        dwarf_attr.update(
            {'luck_total': int(d['luck_base'] * d['luck_multiplier'] + d['luck_bonus'])})
    with transaction.atomic():
        for attribute, total in dwarf_attr.items():
            Dwarf.objects.filter(id=dwarf_id).update(**{attribute: total})

    # Updated data without making a separate query.
    dwarf_info.update(**dwarf_attr)

    return render(request, "dwarves/dwarf.html", {
        'warband': warband,
        'dwarf': dwarf_info,
        'equipment': equipment
    })
