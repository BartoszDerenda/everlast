from django.urls import path
from .views import barracks, details

urlpatterns = [
    path('barracks/', barracks, name="barracks"),
    path('details/', barracks, name="details"),
]