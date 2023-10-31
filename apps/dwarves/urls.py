from django.urls import path
from .views import barracks, dwarf

urlpatterns = [
    path('barracks/', barracks, name="barracks"),
    path('dwarf/<int:dwarf_id>', dwarf, name="dwarf")
]