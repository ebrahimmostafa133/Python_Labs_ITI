from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    total = serializers.FloatField(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'email', 'image', 'date_added', 'total']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
