from rest_framework import serializers
from .models import Student, UserProfile

class StudentSerializer(serializers.ModelSerializer):
    total = serializers.FloatField(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email', 'image', 'date_added', 'total']

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'username']
