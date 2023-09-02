from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=32)
    email = models.EmailField(_('email_address'), unique=True, max_length=254)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

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
    """Is the user a admin member?"""
    return self.admin


def __str__(self):
    return self.username
