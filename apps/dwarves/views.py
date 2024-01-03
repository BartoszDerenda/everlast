import roman

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.db.models.functions import Round
from django.db import transaction
from django.db.models import F
from django.shortcuts import render

from apps.accounts.models import Account, Treasury
from apps.dwarves.models import Dwarf
from apps.dwarves.forms import CreateWarband, EquipmentForm
from apps.items.models import Armor, Weapon, Rune


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
                        Dwarf.objects.filter(id=new_warband[dwarf].id).update(intelligence_base=F('intelligence_base') + 5,
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

    x = Treasury.objects.filter(user_id=request.user.id).values()
    for query in x:
        content_type = ContentType.objects.filter(id=query['content_type_id'])
        print(query)
        print(content_type)

    equipment_form = EquipmentForm(user_id=request.user.id)
    if request.method == 'POST':
        equipment_form = EquipmentForm(request.POST)
        if equipment_form.is_valid():
            pass
        else:
            equipment_form = EquipmentForm(user_id=request.user.id)

    # Query items from inventory that can be equipped
    armor_list = {}
    weapon_list = {}
    rune_list = {}

    # query = Account.objects.filter(id=request.user.id).values('treasury')[0]
    # for key, treasury in query.items():
    # for item, quantity in treasury.items():
    # if Armor.objects.filter(name=item).exists():
    #  armor_list.update({item: quantity})
    # elif Weapon.objects.filter(name=item).exists():
    #     weapon_list.update({item: quantity})
    # elif Rune.objects.filter(name=item).exists():
    #    rune_list.update(({item: quantity}))

    def equip_items(item_name):
        # Update Dwarf attributes based off of the equipped items.
        armor_stats = Armor.objects.filter(name=item_name).values('strength_multiplier', 'strength_bonus',
                                                                  'intelligence_multiplier', 'intelligence_bonus',
                                                                  'endurance_multiplier', 'endurance_bonus',
                                                                  'speed_multiplier', 'speed_bonus',
                                                                  'agility_multiplier', 'agility_bonus',
                                                                  'willpower_multiplier', 'willpower_bonus',
                                                                  'charisma_multiplier', 'charisma_bonus',
                                                                  'luck_multiplier', 'luck_bonus',
                                                                  'physical_armor', 'magical_armor')
        armor_attributes = armor_stats[0]
        dwarf_attributes = Dwarf.objects.filter(id=dwarf_id).values()
        dwarf_attributes.update(
            strength_multiplier=Round(F('strength_multiplier') + armor_attributes['strength_multiplier'], 2),
            strength_bonus=F('strength_bonus') + armor_attributes['strength_bonus'],
            intelligence_multiplier=Round(F('intelligence_multiplier') + armor_attributes['intelligence_multiplier'],
                                          2),
            intelligence_bonus=F('intelligence_bonus') + armor_attributes['intelligence_bonus'],
            endurance_multiplier=Round(F('endurance_multiplier') + armor_attributes['endurance_multiplier'], 2),
            endurance_bonus=F('endurance_bonus') + armor_attributes['endurance_bonus'],
            speed_multiplier=Round(F('speed_multiplier') + armor_attributes['speed_multiplier'], 2),
            speed_bonus=F('speed_bonus') + armor_attributes['speed_bonus'],
            agility_multiplier=Round(F('agility_multiplier') + armor_attributes['agility_multiplier'], 2),
            agility_bonus=F('agility_bonus') + armor_attributes['agility_bonus'],
            willpower_multiplier=Round(F('willpower_multiplier') + armor_attributes['willpower_multiplier'], 2),
            willpower_bonus=F('willpower_bonus') + armor_attributes['willpower_bonus'],
            charisma_multiplier=Round(F('charisma_multiplier') + armor_attributes['charisma_multiplier'], 2),
            charisma_bonus=F('charisma_bonus') + armor_attributes['charisma_bonus'],
            luck_multiplier=Round(F('luck_multiplier') + armor_attributes['luck_multiplier'], 2),
            luck_bonus=F('luck_bonus') + armor_attributes['luck_bonus'],
            physical_armor=F('physical_armor') + armor_attributes['physical_armor'],
            magical_armor=F('magical_armor') + armor_attributes['magical_armor']
        )

    # Equipment
    equipped_items = Dwarf.objects.filter(id=dwarf_id).values('head', 'shoulders', 'chest', 'gloves',
                                                              'pants', 'boots', 'trinket')
    equipment = {}
    for eq_piece in equipped_items:
        for slot, item_name in eq_piece.items():
            if Armor.objects.filter(name=item_name).exists():
                # Add equipped item into the dictionary used in the context.
                equipment.update({slot: Armor.objects.get(name=item_name)})
                # armor_enhancements = Armor.objects.filter(name=item_name).values('enhancements')
                # Dwarf.objects.filter(id=dwarf_id).update(**armor_enhancements)
            else:
                # If no item was found, update context with "No armor" on that slot.
                equipment.update({slot: "No " + slot + " is equipped."})

    # Updating total attributes
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
        'equipment': equipment,
        'equipment_form': equipment_form
    })
