from django.db import models

from accounts.models import Account


def attributes_base():
    return {"strength_base": 1, "intelligence_base": 1, "agility_base": 1, "willpower_base": 1, "endurance_base": 1,
            "charisma_base": 1, "luck_base": 1, "speed_base": 1}


def attributes_trained():
    return {"strength_trained": 0, "intelligence_trained": 0, "agility_trained": 0, "willpower_trained": 0,
            "endurance_trained": 0, "charisma_trained": 0, "luck_trained": 0, "speed_trained": 0}


def attribute_multipliers():
    return {"strength_multiplier": 0, "intelligence_multiplier": 0, "agility_multiplier": 0, "willpower_multiplier": 0,
            "endurance_multiplier": 0, "charisma_multiplier": 0, "luck_multiplier": 0, "speed_multiplier": 0}


def attributes_total():
    return {"strength_total": 0, "intelligence_total": 0, "agility_total": 0, "willpower_total": 0,
            "endurance_total": 0, "charisma_total": 0, "luck_total": 0, "speed_total": 0}


def default_status():
    return {'idle': None}


def equipment():
    return {"head": None,
            "shoulders": None,
            "chest": None,
            "gloves": None,
            "pants": None,
            "boots": None,
            "weapon": {
                "main_hand": None,
                "off_hand": None,
                "two_hand": None
            },
            "artifact": None,
            }


class Dwarf(models.Model):
    name = models.CharField(max_length=32)
    leader = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    status = models.JSONField(default=default_status)

    equipment = models.JSONField(default=equipment)

    attributes_base = models.JSONField(default=attributes_base)
    attributes_trained = models.JSONField(default=attributes_trained)
    attribute_multipliers = models.JSONField(default=attribute_multipliers)
    attributes_total = models.JSONField(default=attributes_total)

    physical_armor = models.FloatField(default=0.00)
    magical_armor = models.FloatField(default=0.00)

    ability_cap = models.IntegerField(default=0)
    abilities = models.JSONField(default=dict, blank=True)
