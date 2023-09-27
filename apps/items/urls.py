from django.urls import path
from .views import treasury

urlpatterns = [
    path('treasury/', treasury, name='treasury'),
]