from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


def treasury_template():
    return {'Iron Ore': 999, 'Iron Ingot': 999, 'Oak Wood': 0, 'Oak Plank': 999, 'Meteorite Ingot': 999,
            'Oakbrew': 999,

            'Iron Tasset': 2, 'Iron Helmet': 0, 'Dragonscale Chestplate': 14,

            'Iron Mace': 0, 'Oak Staff': 10, 'Flameberg': 4,
            }


def known_recipes_template():
    return {'Iron Ingot': True, 'Oak Plank': True, 'Meteorite Ingot': True,

            'Iron Tasset': False, 'Iron Helmet': True, 'Dragonscale Chestplate': True,

            'Iron Mace': True, 'Oak Staff': False, 'Flameberg': True,
            }


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=32)
    email = models.EmailField(_('email_address'), unique=True, max_length=255)
    avatar = models.ImageField(upload_to='static/avatars', default='static/placeholder.png')

    profile_text = models.TextField(max_length=4096, blank=True)
    last_visited = models.JSONField(default=dict, blank=True)

    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    warband = models.JSONField(default=list, blank=True)
    treasury = models.JSONField(default=treasury_template)
    known_recipes = models.JSONField(default=known_recipes_template)

    gold = models.IntegerField(default=0)
    rubies = models.IntegerField(default=0)

    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    perk_points = models.IntegerField(default=1)
    adventuring_perks = models.IntegerField(default=0)
    combat_perks = models.IntegerField(default=0)
    crafting_perks = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True


def is_staff(self):
    """Is the user a member of staff?"""
    return self.staff


@property
def is_admin(self):
    """Is the user an admin member?"""
    return self.admin


def __str__(self):
    return self.username
