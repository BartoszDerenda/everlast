from django.contrib import admin
from items.models import Material, Armor, Weapon

# Register your models here.
admin.site.register(Material)
admin.site.register(Armor)
admin.site.register(Weapon)
