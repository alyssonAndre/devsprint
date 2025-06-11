from django.urls import path
from .api import *

urlpatterns = [
    path('progress/', UserProgressAPI.as_view(), name='lesson-progress'),
    path('submit/', CodeSubmissionAPI.as_view(), name='code-submission'),
]