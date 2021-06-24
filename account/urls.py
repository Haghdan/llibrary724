
from django.urls import path
from . import views
from .views import log_out, login_user, register, user_profile, user_update_profile

urlpatterns = [
    path('login', login_user),
    path('log-out', log_out),
    path('register', register),
    path('profile', user_profile),
    path('update_profile', user_update_profile),
]
