from django.urls import path
from .views import index, sign_up, sign_in, sign_out, activate

urlpatterns = [
    path('mountain', index, name="index"),
    path('signup/', sign_up, name="signup"),
    path('login/', sign_in, name="login"),
    path('logout/', sign_out, name='logout'),
    path('form/', index, name='index'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]