from django.db import models


def base_attributes():
    return {"base_str": 1, "base_int": 1, "base_agi": 1, "base_will": 1, "base_end": 1, "base_char": 1, "base_lck": 1,
            "base_spd": 1}


def trained_attributes():
    return {"trained_str": 0, "trained_int": 0, "trained_agi": 0, "trained_will": 0, "trained_end": 0,
            "trained_char": 0, "trained_lck": 0, "trained_spd": 0}


def default_equipment():
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
            "artifact_1": None,
            "artifact_2": None
            }


class Dwarf(models.Model):
    name = models.CharField(max_length=32)
    leader = models.TextField()
    level = models.IntegerField()

    base_attributes = models.JSONField(default=base_attributes)
    trained_attributes = models.JSONField(default=trained_attributes)

    tactic = models.TextField(default="Frenzy")
    equipment = models.JSONField(default=default_equipment)
