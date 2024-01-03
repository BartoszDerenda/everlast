from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from ..items.models import Recipe
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


def treasury_template():
    return {'Iron Ore': 999, 'Iron Ingot': 999, 'Oak Wood': 0, 'Oak Plank': 999, 'Meteorite Ingot': 999,
            'Oakbrew': 999,

            'Iron Tasset': 2, 'Iron Helmet': 0, 'Dragonscale Chestplate': 14,

            'Iron Mace': 0, 'Oak Staff': 10, 'Flameberg': 4,
            }


def known_recipes_template():
    return ['Iron Ingot', 'Oak Plank', 'Meteorite Ingot',

            'Iron Tasset', 'Iron Helmet', 'Dragonscale Chestplate',

            'Iron Mace', 'Oak Staff', 'Flameberg'
            ]


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=32)
    email = models.EmailField(_('email_address'), unique=True, max_length=255)
    avatar = models.ImageField(upload_to='static/avatars', default='static/avatars/placeholder.png')

    profile_text = models.TextField(max_length=4096, blank=True)
    reputation = models.IntegerField(default=0)

    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

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


class Comment(models.Model):
    author = models.ForeignKey(Account, related_name='author', null=True, on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(Account, related_name='receiver', null=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=255, blank=True)
    points = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=timezone.now)


class Guestbook(models.Model):
    profile = models.ForeignKey(Account, related_name='profile', null=True, on_delete=models.CASCADE)
    guest = models.ForeignKey(Account, related_name='guest', null=True, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(default=timezone.now)


class Treasury(models.Model):
    user = models.ForeignKey(Account, related_name='owner', null=False, on_delete=models.DO_NOTHING)
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=64, null=True)
    item_type = models.CharField(max_length=32, null=True)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Treasury"
        verbose_name_plural = "Treasuries"


class KnownRecipes(models.Model):
    user = models.ForeignKey(Account, related_name='user', null=False, on_delete=models.DO_NOTHING)
    recipe = models.ForeignKey(Recipe, related_name='item', null=False, on_delete=models.DO_NOTHING)
    known = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Known recipe"
        verbose_name_plural = "Known recipes"


def is_staff(self):
    """Is the user a member of staff?"""
    return self.staff


@property
def is_admin(self):
    """Is the user an admin member?"""
    return self.admin


def __str__(self):
    return self.username
