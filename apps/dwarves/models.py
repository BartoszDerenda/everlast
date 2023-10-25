import random

from django.db import models

from apps.accounts.models import Account


def initial_attributes():
    return int(random.randint(10, 15))


class Character(models.Model):
    # Total attributes
    strength_total = models.IntegerField(default=0)
    intelligence_total = models.IntegerField(default=0)
    endurance_total = models.IntegerField(default=0)
    speed_total = models.IntegerField(default=0)
    agility_total = models.IntegerField(default=0)
    willpower_total = models.IntegerField(default=0)
    charisma_total = models.IntegerField(default=0)
    luck_total = models.IntegerField(default=0)

    # Armor
    physical_armor = models.IntegerField(default=0)
    magical_armor = models.IntegerField(default=0)
    physical_mitigation = models.FloatField(default=0.00)
    magical_mitigation = models.FloatField(default=0.00)

    # List of abilities
    abilities = models.JSONField(default=dict, blank=True)

    class Meta:
        abstract = True


class Dwarf(Character):
    # Basic info
    name = models.CharField(max_length=32)
    leader = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=32)
    status_time = models.DateTimeField(null=True, blank=True)

    # Battles' history
    pvp_points = models.IntegerField(default=0)
    battles_fought = models.IntegerField(default=0)
    battles_won = models.IntegerField(default=0)

    # Equipment
    head = models.CharField(max_length=64, blank=True, null=True)
    shoulders = models.CharField(max_length=64, blank=True, null=True)
    chest = models.CharField(max_length=64, blank=True, null=True)
    gloves = models.CharField(max_length=64, blank=True, null=True)
    pants = models.CharField(max_length=64, blank=True, null=True)
    boots = models.CharField(max_length=64, blank=True, null=True)
    two_hand = models.CharField(max_length=64, blank=True, null=True)
    main_hand = models.CharField(max_length=64, blank=True, null=True)
    off_hand = models.CharField(max_length=64, blank=True, null=True)
    trinket = models.CharField(max_length=64, blank=True, null=True)

    # Attributes
    strength_base = models.IntegerField(default=initial_attributes)
    intelligence_base = models.IntegerField(default=initial_attributes)
    endurance_base = models.IntegerField(default=initial_attributes)
    speed_base = models.IntegerField(default=initial_attributes)
    agility_base = models.IntegerField(default=initial_attributes)
    willpower_base = models.IntegerField(default=initial_attributes)
    charisma_base = models.IntegerField(default=initial_attributes)
    luck_base = models.IntegerField(default=initial_attributes)

    strength_multiplier = models.IntegerField(default=0)
    intelligence_multiplier = models.IntegerField(default=0)
    endurance_multiplier = models.IntegerField(default=0)
    speed_multiplier = models.IntegerField(default=0)
    agility_multiplier = models.IntegerField(default=0)
    willpower_multiplier = models.IntegerField(default=0)
    charisma_multiplier = models.IntegerField(default=0)
    luck_multiplier = models.IntegerField(default=0)

    strength_bonus = models.IntegerField(default=0)
    intelligence_bonus = models.IntegerField(default=0)
    endurance_bonus = models.IntegerField(default=0)
    speed_bonus = models.IntegerField(default=0)
    agility_bonus = models.IntegerField(default=0)
    willpower_bonus = models.IntegerField(default=0)
    charisma_bonus = models.IntegerField(default=0)
    luck_bonus = models.IntegerField(default=0)

    # Abilities and BP
    ability_cap = models.IntegerField(default=0)
    battle_power = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# PvE enemies do not need variables such as attribute multipliers, bonuses or even equipment.
# All they need is the outcome of such mathematics - total attributes and list of abilities they possess.
# No player will ever change equipment pieces of a non-playable character.
# This may be problematic once I start thinking about implementing a way to disarm the opponent.
# (Perhaps every single mob would have a hard-coded response to disarm, that would take away a portion of their)
# (attributes and maybe a specific ability?)
class Monster(Character):
    name = models.CharField(max_length=64)
    zone = models.CharField(max_length=64, blank=True, null=True)
    mob_type = models.CharField(max_length=16, default='normal')  # Normal / Boss / idk
    race = models.CharField(max_length=16, default='monster', null=True, blank=True)

    def __str__(self):
        return self.name
