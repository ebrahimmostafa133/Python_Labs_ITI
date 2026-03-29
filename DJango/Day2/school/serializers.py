from rest_framework import serializers
from .models import Student ,Subject, Grade, Feedback, UserProfile

class StudentSerializer(serializers.ModelSerializer):
    total = serializers.FloatField(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email', 'image', 'date_added', 'total']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description']

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

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'username']
