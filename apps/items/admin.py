from django.contrib import admin
from apps.items.models import Material, Armor, Weapon, Rune, Recipe


class CustomEquipmentAdmin(admin.ModelAdmin):
    list_display = ["name", "item_slot", "rarity", "id"]


class CustomItemAdmin(admin.ModelAdmin):
    list_display = ["name", "rarity", "id"]


admin.site.register(Material, CustomItemAdmin)
admin.site.register(Armor, CustomEquipmentAdmin)
admin.site.register(Weapon, CustomEquipmentAdmin)
admin.site.register(Rune, CustomItemAdmin)
admin.site.register(Recipe, CustomItemAdmin)
