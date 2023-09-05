from django.db import models


class Weapon(models.Model):
    name = models.CharField(max_length=64, unique=True)
    item_type = models.CharField(max_length=16, default='weapon')
    item_slot = models.JSONField(default=list)  # For when an item can be main hand and off-hand.
    rarity = models.CharField(max_length=16)
    tooltip = models.CharField(max_length=255)

    attr_bonus = models.JSONField(default=dict)
    attr_multi = models.JSONField(default=dict)
    abilities = models.JSONField(default=dict, null=True, blank=True)

    materials = models.JSONField(default=dict, null=True, blank=True)


class Armor(models.Model):
    name = models.CharField(max_length=64, unique=True)
    item_type = models.CharField(max_length=16, default='armor')
    item_slot = models.CharField(max_length=16)
    rarity = models.CharField(max_length=16)
    tooltip = models.CharField(max_length=255)

    attr_bonus = models.JSONField(default=dict)
    attr_multi = models.JSONField(default=dict)
    armor_values = models.JSONField(default=dict)
    abilities = models.JSONField(default=dict, null=True, blank=True)

    materials = models.JSONField(default=dict, null=True, blank=True)


class Material(models.Model):
    name = models.CharField(max_length=64, unique=True)
    item_type = models.CharField(max_length=16, default='material')
    rarity = models.CharField(max_length=16)
    tooltip = models.CharField(max_length=255)

    materials = models.JSONField(default=dict, null=True, blank=True)  # For refined materials.


class Rune(models.Model):
    name = models.CharField(max_length=64, unique=True)
    item_type = models.CharField(max_length=16, default='rune')
    rarity = models.CharField(max_length=16)
    tooltip = models.CharField(max_length=255)

    materials = models.JSONField(default=dict, null=True, blank=True)


class Recipe(models.Model):
    name = models.CharField(max_length=64, unique=True)
    item_type = models.CharField(max_length=16, default='recipe')
    rarity = models.CharField(max_length=16)
    tooltip = models.CharField(max_length=255)

    recipe_for = models.CharField(max_length=64, unique=True)
    ingredients_required = models.JSONField(default=dict)

    materials = models.JSONField(default=dict, null=True, blank=True)
