from django.urls import path
from .api import *

urlpatterns = [
    path('profile/', UserDetailView.as_view(), name='user-profile-api'),
    path('register/', UserRegisterAPI.as_view(), name='user-register-api'),
]
