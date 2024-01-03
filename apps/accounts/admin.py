from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.models import Account, Comment, Guestbook, Treasury, KnownRecipes
from apps.authentication.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account

    list_display = ['username', 'email', 'is_staff', 'is_active', ]
    list_filter = ['username', 'email', 'is_staff', 'is_active', ]
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


class CustomCommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'receiver', 'timestamp']
    fieldsets = [
        ['User info', {'fields': ('author', 'receiver')}],
        ['Comment', {'fields': ('text', 'points', 'timestamp')}]
    ]


class CustomGuestbookAdmin(admin.ModelAdmin):
    list_display = ['profile', 'guest', 'timestamp']


class CustomTreasuryAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'item_type', 'quantity']


class CustomKnownRecipesAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipe', 'known']


admin.site.register(Account, CustomUserAdmin)
admin.site.register(Comment, CustomCommentAdmin)
admin.site.register(Guestbook, CustomGuestbookAdmin)
admin.site.register(Treasury, CustomTreasuryAdmin)
admin.site.register(KnownRecipes, CustomKnownRecipesAdmin)
