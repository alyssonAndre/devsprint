from rest_framework import serializers
from .models import *

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = '__all__'
        read_only_fields = ('user', 'completed_at')


class SubmissionSerializer(serializers.ModelSerializer):
    function_name = serializers.CharField(write_only=True)
    test_cases = serializers.ListField(
        child=serializers.DictField(child=serializers.JSONField()),
        write_only=True
    )
    
    class Meta:
        model = ExerciseSubmission
        fields = ['module_id', 'lesson_id', 'exercise_id', 'source_code', 'function_name', 'test_cases']
        read_only_fields = ['user', 'submitted_at']

    def validate_test_cases(self, value):
        for i, case in enumerate(value, start=1):
            if not isinstance(case, dict):
                raise serializers.ValidationError(f"Test case {i} must be a dictionary.")
            if 'inputs' not in case:
                raise serializers.ValidationError(f"Test case {i} missing 'inputs' key.")
            if 'expected' not in case:
                raise serializers.ValidationError(f"Test case {i} missing 'expected' key.")
        return value
