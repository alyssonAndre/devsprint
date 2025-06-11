from django.urls import path
from .api import UserProfileDetailAPI

urlpatterns = [
    path('profile/', UserProfileDetailAPI.as_view(), name='user-profile-api'),
]
