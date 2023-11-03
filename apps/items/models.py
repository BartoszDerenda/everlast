from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=64, unique=True)
    rarity = models.CharField(max_length=16)
    tooltip = models.CharField(max_length=255)
    crafting = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        abstract = True


class Weapon(Item):
    icon = models.ImageField(upload_to='static/images/item-icons/weapon-icons', default='static/images/item-icons'
                                                                                        '/weapon-icons/placeholder.png')
    item_type = models.CharField(max_length=16, default='weapon')
    item_slot = models.CharField(max_length=16, default='weapon')
    # For the future when I implement off-hand, two-hand and main-hand weapons.

    strength_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    intelligence_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    endurance_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    speed_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    agility_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    willpower_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    charisma_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    luck_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    strength_bonus = models.IntegerField(default=0)
    intelligence_bonus = models.IntegerField(default=0)
    endurance_bonus = models.IntegerField(default=0)
    speed_bonus = models.IntegerField(default=0)
    agility_bonus = models.IntegerField(default=0)
    willpower_bonus = models.IntegerField(default=0)
    charisma_bonus = models.IntegerField(default=0)
    luck_bonus = models.IntegerField(default=0)

    physical_armor = models.IntegerField(null=True, blank=True)
    magical_armor = models.IntegerField(null=True, blank=True)

    enhancements = models.JSONField(default=dict, null=True, blank=True)


class Armor(Item):
    icon = models.ImageField(upload_to='static/images/item-icons/armor-icons', default='static/images/item-icons'
                                                                                       '/armor-icons/placeholder.png')
    item_type = models.CharField(max_length=16, default='armor')
    item_slot = models.CharField(max_length=16)

    strength_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    intelligence_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    endurance_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    speed_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    agility_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    willpower_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    charisma_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    luck_multiplier = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    strength_bonus = models.IntegerField(default=0)
    intelligence_bonus = models.IntegerField(default=0)
    endurance_bonus = models.IntegerField(default=0)
    speed_bonus = models.IntegerField(default=0)
    agility_bonus = models.IntegerField(default=0)
    willpower_bonus = models.IntegerField(default=0)
    charisma_bonus = models.IntegerField(default=0)
    luck_bonus = models.IntegerField(default=0)

    physical_armor = models.IntegerField()
    magical_armor = models.IntegerField()

    enhancements = models.JSONField(default=dict, null=True, blank=True)


class Material(Item):
    icon = models.ImageField(upload_to='static/images/item-icons/material-icons', default='static/images/item-icons'
                                                                                          '/material-icons'
                                                                                          '/placeholder.png')
    item_type = models.CharField(max_length=16, default='material')


class Rune(Item):
    icon = models.ImageField(upload_to='static/images/item-icons/rune-icons', default='static/images/item-icons'
                                                                                      '/rune-icons/placeholder.png')
    item_type = models.CharField(max_length=16, default='rune')
    enhancements = models.JSONField(default=dict, null=True, blank=True)


class Recipe(Item):
    icon = models.ImageField(upload_to='static/images/item-icons/recipe-icons', default='static/images/item-icons'
                                                                                        '/recipe-icons/placeholder.png')
    item_type = models.CharField(max_length=16, default='recipe')

    recipe_for = models.CharField(max_length=64)
    recipe_materials = models.JSONField(default=dict)


class Enhancement(models.Model):
    name = models.CharField(max_length=32)
    power = models.IntegerField()
    effect = models.TextField(max_length=128)
