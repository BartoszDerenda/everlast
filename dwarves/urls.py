from django.urls import path
from .views import barracks

urlpatterns = [
    path('barracks/', barracks, name="barracks"),
]