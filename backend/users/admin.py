from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'telefone', 'data_nascimento', 'sexo')
    search_fields = ('user__username', 'email')
    list_filter = ('sexo',)
    ordering = ('-id',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
    
    
