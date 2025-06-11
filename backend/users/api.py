from rest_framework import generics, permissions
from .serializers import *


class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  
    
    

class UserRegisterAPI(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

