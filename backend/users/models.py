from django.db import models
from django.contrib.auth.models import User
from common.models import SoftDeleteModel


class UserProfile(SoftDeleteModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')], blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    


