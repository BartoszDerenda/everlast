from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=64, unique=True)
    rarity = models.CharField(max_length=16)
    tooltip = models.CharField(max_length=255)
    crafting = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        abstract = True


class Weapon(Item):
    item_type = models.CharField(max_length=16, default='weapon')
    item_slot = models.JSONField(default=list)  # For when an item can be main hand and off-hand.

    attr_bonus = models.JSONField(default=dict)
    attr_multi = models.JSONField(default=dict)

    physical_armor = models.IntegerField(null=True, blank=True)
    magical_armor = models.IntegerField(null=True, blank=True)

    enhancements = models.JSONField(default=dict, null=True, blank=True)


class Armor(Item):
    item_type = models.CharField(max_length=16, default='armor')
    item_slot = models.CharField(max_length=16)

    attr_bonus = models.JSONField(default=dict)
    attr_multi = models.JSONField(default=dict)

    physical_armor = models.IntegerField()
    magical_armor = models.IntegerField()

    enhancements = models.JSONField(default=dict, null=True, blank=True)


class Material(Item):
    item_type = models.CharField(max_length=16, default='material')


class Rune(Item):
    item_type = models.CharField(max_length=16, default='rune')


class Recipe(Item):
    item_type = models.CharField(max_length=16, default='recipe')

    recipe_for = models.CharField(max_length=64)
    recipe_materials = models.JSONField(default=dict)
