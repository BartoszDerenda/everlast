from django.urls import path
from .views import shrine

urlpatterns = [
    path('shrine/', shrine, name="shrine"),
]