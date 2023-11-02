from django.contrib import admin
from apps.dwarves.models import Dwarf, Monster


class CustomDwarfAdmin(admin.ModelAdmin):
    list_display = ["name", "leader", "id"]
    fieldsets = [
        ['Info', {'fields': ('name', 'leader')}],
        ['Status', {'fields': ('status', 'status_time')}],
        ['PvP', {'fields': ('pvp_points', 'battles_fought', 'battles_won')}],
        ['Equipment', {'fields': ('head', 'shoulders', 'chest', 'gloves', 'pants', 'boots',
                                  'weapon', 'trinket', 'title')}],
        ['Abilities', {'fields': ['abilities', 'ability_cap']}],
        ['Armor', {'fields': ['physical_armor', 'physical_mitigation',
                              'magical_armor', 'magical_mitigation']}],
        ['Attributes base', {'fields': ('strength_base', 'intelligence_base', 'endurance_base',
                                        'speed_base', 'agility_base', 'willpower_base',
                                        'charisma_base', 'luck_base')}],
        ['Attributes multipliers', {'fields': ('strength_multiplier', 'intelligence_multiplier', 'endurance_multiplier',
                                               'speed_multiplier', 'agility_multiplier', 'willpower_multiplier',
                                               'charisma_multiplier', 'luck_multiplier')}],
        ['Attributes bonus', {'fields': ('strength_bonus', 'intelligence_bonus', 'endurance_bonus',
                                         'speed_bonus', 'agility_bonus', 'willpower_bonus',
                                         'charisma_bonus', 'luck_bonus')}],
        ['Attributes total', {'fields': ('strength_total', 'intelligence_total', 'endurance_total',
                                         'speed_total', 'agility_total', 'willpower_total',
                                         'charisma_total', 'luck_total')}],
        ['Battle power', {'fields': ['battle_power']}]
    ]

    add_fieldsets = [
        ['Info', {'fields': ('name', 'leader')}],
        ['PvP', {'fields': ('pvp_points', 'battles_fought', 'battles_won')}],
        ['Equipment', {'fields': ('head', 'shoulders', 'chest', 'gloves', 'pants', 'boots',
                                  'two_hand', 'main_hand', 'off_hand', 'trinket', 'title')}],
        ['Attributes base', {'fields': ('strength_base', 'intelligence_base', 'endurance_base',
                                        'speed_base', 'agility_base', 'willpower_base',
                                        'charisma_base', 'luck_base')}]
    ]


class CustomMonsterAdmin(admin.ModelAdmin):
    list_display = ["name", "mob_type", "race", "zone", "id"]
    fieldsets = [
        ['Info', {'fields': ('name', 'mob_type', 'race', 'zone')}],
        ['Abilities', {'fields': ['abilities']}],
        ['Armor', {'fields': ['physical_armor', 'physical_mitigation',
                              'magical_armor', 'magical_mitigation']}],
        ['Attributes total', {'fields': ('strength_total', 'intelligence_total', 'endurance_total',
                                         'speed_total', 'agility_total', 'willpower_total',
                                         'charisma_total', 'luck_total')}],
        ['Battle power', {'fields': ['battle_power']}]
    ]

    add_fieldsets = [
        ['Info', {'fields': ('name', 'mob_type', 'race', 'zone')}],
        ['Abilities', {'fields': ['abilities']}],
        ['Armor', {'fields': ['physical_armor', 'physical_mitigation',
                              'magical_armor', 'magical_mitigation']}],
        ['Attributes total', {'fields': ('strength_total', 'intelligence_total', 'endurance_total',
                                         'speed_total', 'agility_total', 'willpower_total',
                                         'charisma_total', 'luck_total')}]
    ]


admin.site.register(Dwarf, CustomDwarfAdmin)
admin.site.register(Monster, CustomMonsterAdmin)
