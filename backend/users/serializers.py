from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from datetime import date

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'telefone', 'data_nascimento', 'sexo']



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    telefone = serializers.CharField(required=False, allow_blank=True)
    data_nascimento = serializers.DateField(required=False, allow_null=True)
    sexo = serializers.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Feminino')], required=False, allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'telefone', 'data_nascimento', 'sexo']

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("O campo de email é obrigatório.")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Já existe um usuário com esse email.")
        return value
    
    def validate_data_nascimento(self, value):
        if value and value > date.today():
            raise serializers.ValidationError("A data de nascimento não pode ser no futuro.")
        return value

    def create(self, validated_data):
        
        telefone = validated_data.pop('telefone', None)
        data_nascimento = validated_data.pop('data_nascimento', None)
        sexo = validated_data.pop('sexo', None)
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name', '')
        last_name = validated_data.pop('last_name', '')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        UserProfile.objects.create(
            user=user,
            telefone=telefone or '',
            data_nascimento=data_nascimento,
            sexo=sexo or '',
            email=user.email 
        )

        return user
