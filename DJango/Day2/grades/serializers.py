from rest_framework import serializers
from .models import Grade, Feedback

class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    subject_name = serializers.ReadOnlyField(source='subject.name')
    class Meta:
        model = Grade
        fields = ['id', 'student', 'subject', 'value', 'date_added', 'student_name', 'subject_name']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'email', 'message', 'date_added']
