from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.dwarves.models import Dwarf
from apps.items.models import Weapon, Armor, Material, Rune, Recipe
from apps.accounts.models import Account


@login_required(login_url='/mountain', redirect_field_name=None)
def treasury(request):
    warband = Dwarf.objects.filter(leader=request.user).values('id', 'name', 'status')
    treasury_list = Account.objects.filter(id=request.user.id).values_list('treasury', flat=True).first()
    owned_items = {key: val for key, val in treasury_list.items()
                   if val != 0}

    print(owned_items)

    materials_list = Material.objects.all().values()
    weapons_list = Weapon.objects.all().values()
    armors_list = Armor.objects.all().values()
    runes_list = Rune.objects.all().values()
    recipes_list = Recipe.objects.all().values()

    owned_materials = []
    owned_weapons = []
    owned_armors = []
    owned_runes = []
    owned_recipes = []

    def item_type_list_generator(type_list, owned_list):
        for key in owned_items:
            for item in type_list:
                if item["name"] == key:
                    item.update({'quantity': owned_items.get(key)})
                    owned_list.append(item)
        return owned_list

    item_type_list_generator(materials_list, owned_materials)
    item_type_list_generator(weapons_list, owned_weapons)
    item_type_list_generator(armors_list, owned_armors)
    item_type_list_generator(runes_list, owned_runes)
    item_type_list_generator(recipes_list, owned_recipes)

    return render(request, "../templates/items/treasury.html", {
        'warband': warband,
        'owned_materials': owned_materials,
        'owned_weapons': owned_weapons,
        'owned_armors': owned_armors,
        'owned_runes': owned_runes,
        'owned_recipes': owned_recipes
    })
