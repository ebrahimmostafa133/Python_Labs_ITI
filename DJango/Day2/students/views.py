from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Sum

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token

from .models import Student, UserProfile
from .serializers import (
    StudentSerializer, UserProfileSerializer, 
    UserSerializer, UserRegisterSerializer
)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_api(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "msg": "Login Success",
            "user": UserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_200_OK)
    return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@login_required
def home(request):
    return render(request, "students/home.html")

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect("login")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "students/login.html", {"form": form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "students/register.html", {"form": form})

@login_required
def profile_view(request):
    return render(request, "students/userProfile.html")

@login_required
def students_view(request):
    msg = None
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        image = request.FILES.get("image")
        Student.objects.create(name=name, age=age, email=email, image=image)
        msg = "Student added successfully!"
    students = Student.objects.all()
    return render(request, "students/students.html", {"students": students, "msg": msg})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("students")

@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.email = request.POST.get("email")
        if request.FILES.get("image"):
            student.image = request.FILES.get("image")
        student.save()
        return redirect("students")
    return render(request, "students/student_edit.html", {"student": student, "is_edit": True})

@login_required
def leaderboard_view(request):
    top_students = Student.get_top_students()
    return render(request, "students/leaderboard.html", {"top_students": top_students})

@api_view(['GET', 'POST'])
def student_api_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_api_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.get_top_students()
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.get_top_students()

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
