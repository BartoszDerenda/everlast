from django.urls import path
from .views import settings, profile

urlpatterns = [
    path('settings/', settings, name="settings"),
    path('profile/<int:id>', profile, name="profile"),
]