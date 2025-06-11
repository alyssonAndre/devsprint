from django.contrib import admin
from .models import *


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'module_id', 'is_completed', 'completed_at')
    search_fields = ('user__username', 'module_id')
    list_filter = ('is_completed',)
    ordering = ('-completed_at',)


@admin.register(ExerciseSubmission)
class ExerciseSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'module_id', 'lesson_id', 'exercise_id', 'is_correct', 'submitted_at')
    search_fields = ('user__username', 'module_id', 'lesson_id', 'exercise_id')
    list_filter = ('is_correct',)
    ordering = ('-submitted_at',)
