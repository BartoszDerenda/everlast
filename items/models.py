from django.db import models


class Weapon(models.Model):
    name = models.CharField(max_length=64, unique=True)
    item_slot = models.JSONField(default=list)  # For when an item can be main hand and off-hand.
    rarity = models.CharField(max_length=16)
    tooltip = models.CharField(max_length=255)

    attr_bonus = models.JSONField(default=dict)
    attr_multi = models.JSONField(default=dict)
    abilities = models.JSONField(default=dict, null=True, blank=True)

    materials = models.JSONField(default=dict, null=True, blank=True)


class Armor(models.Model):
    name = models.CharField(max_length=64, unique=True)
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
    rarity = models.CharField(max_length=16)
    tooltip = models.CharField(max_length=255)

    materials = models.JSONField(default=dict, null=True, blank=True)  # For refined materials.
