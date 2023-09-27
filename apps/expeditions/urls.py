from django.urls import path
from .views import expeditions

urlpatterns = [
    path('expeditions/', expeditions, name="expeditions"),
]