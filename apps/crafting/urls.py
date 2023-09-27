from django.urls import path
from .views import crafting

urlpatterns = [
    path('crafting/', crafting, name="crafting"),
]