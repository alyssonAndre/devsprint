from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.api_urls')),
    path('api/modules/', include('modules.api_urls')),

]
