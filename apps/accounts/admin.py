from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models import Account, Comment, Guestbook
from apps.authentication.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account

    list_display = ['username', 'email', 'is_staff', 'is_active',]
    list_filter = ['username', 'email', 'is_staff', 'is_active',]
    fieldsets = [
        ['User info', {'fields': ('username', 'email', 'password', 'avatar')}],
        ['Permissions', {'fields': ('is_staff', 'is_active')}],
        ['Profile info', {'fields': ('profile_text', 'reputation')}],
        ['Account info', {'fields': ('treasury', 'gold', 'rubies', 'known_recipes',
                                     'level', 'experience', 'perk_points', 'adventuring_perks', 'combat_perks',
                                     'crafting_perks')}]
    ]
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['username', 'email', 'password1', 'password2', 'is_staff', 'is_active']
        }),
    ]
    search_fields = ['username']
    ordering = ['username']
    filter_horizontal = []


admin.site.register(Account, CustomUserAdmin)
admin.site.register(Comment)
admin.site.register(Guestbook)
