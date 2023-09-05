from django.urls import path
from .views import homepage, treasury

urlpatterns = [
    path('', homepage, name="homepage"),
    path('treasury/', treasury, name='treasury'),
]