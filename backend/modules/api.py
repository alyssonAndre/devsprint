from rest_framework import generics, permissions, status 
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .validators import validate_python_code
from django.utils import timezone

class UserProgressAPI(generics.ListCreateAPIView):
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return UserProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class CodeSubmissionAPI(generics.CreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.validated_data
        
        test_cases = data['test_cases']
        if isinstance(test_cases, dict):
            test_cases = list(test_cases.values())
        
        passed, message = validate_python_code(
            data['source_code'], data['function_name'], test_cases
        )
        
        ExerciseSubmission.objects.create(
            user=request.user,
            module_id=data['module_id'],
            lesson_id=data['lesson_id'],
            exercise_id=data['exercise_id'],
            source_code=data['source_code'],
            is_correct=passed
        )
        
        if passed:
            UserProgress.objects.update_or_create(
                user=request.user,
                module_id=data['module_id'],
                lesson_id=data['lesson_id'],
                exercise_id=data['exercise_id'],
                defaults={'completed_at': timezone.now(),
                          'is_completed': True
                }
            )
            message = "All test cases passed. Progress updated."
        
        return Response({'success': passed, 'message': message}, status=status.HTTP_201_CREATED)