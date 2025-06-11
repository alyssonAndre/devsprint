from django.db import models
from django.conf import settings
from common.models import SoftDeleteModel

class UserProgress(SoftDeleteModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progress')
    module_id = models.CharField(max_length=100)
    lesson_id = models.CharField(max_length=100)
    exercise_id = models.CharField(max_length=100, blank=True, null=True)        
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        unique_together = ('user', 'module_id', 'lesson_id')

    def __str__(self):
        return f"{self.user.username}"
    
    

class ExerciseSubmission(SoftDeleteModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exercise_submissions')
    module_id = models.CharField(max_length=100)         
    lesson_id = models.CharField(max_length=100)       
    exercise_id = models.CharField(max_length=100)        
    source_code = models.TextField()                    
    is_correct = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exercise_id}"