from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Sum

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Student, Subject, Grade, Feedback, UserProfile
from .serializers import (
    StudentSerializer, SubjectSerializer, GradeSerializer,
    FeedbackSerializer, UserProfileSerializer
)


@login_required
def home(request):
    return render(request, "home.html")

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
    return render(request, "login.html", {"form": form})


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
    return render(request, "register.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "userProfile.html")


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
    return render(request, "students.html", {"students": students, "msg": msg})


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

    return render(request, "student_edit.html", {"student": student, "is_edit": True})


@login_required
def subjects_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        Subject.objects.create(name=name, description=description)
        return redirect("subjects")

    subjects = Subject.objects.all()
    return render(request, "subjects.html", {"subjects": subjects})


@login_required
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect("subjects")


@login_required
def subject_edit(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        subject.name = request.POST.get("name")
        subject.description = request.POST.get("description")
        subject.save()
        return redirect("subjects")

    return render(request, "subject_edit.html", {"subject": subject})


@login_required
def grades_view(request):
    search_query = request.GET.get("search", "")
    if request.method == "POST":
        student_id = request.POST.get("student")
        subject_id = request.POST.get("subject")
        value = request.POST.get("value")
        student = get_object_or_404(Student, id=student_id)
        subject = get_object_or_404(Subject, id=subject_id)
        Grade.objects.update_or_create(
            student=student, subject=subject, defaults={"value": value}
        )
        return redirect("grades")

    grades = Grade.objects.all()
    if search_query:
        grades = grades.filter(student__name__icontains=search_query) | grades.filter(
            subject__name__icontains=search_query
        )

    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(
        request,
        "grades.html",
        {
            "grades": grades,
            "students": students,
            "subjects": subjects,
            "search_query": search_query,
        },
    )


@login_required
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    grade.delete()
    return redirect("grades")


@login_required
def grade_edit(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == "POST":
        grade.student_id = request.POST.get("student")
        grade.subject_id = request.POST.get("subject")
        grade.value = request.POST.get("value")
        grade.save()
        return redirect("grades")

    students = Student.objects.all()
    subjects = Subject.objects.all()
    return render(
        request,
        "grade_edit.html",
        {"grade": grade, "students": students, "subjects": subjects},
    )


@login_required
def leaderboard_view(request):
    top_students = Student.get_top_students()
    return render(request, "leaderboard.html", {"top_students": top_students})


def contact_view(request):
    msg = None
    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        Feedback.objects.create(email=email, message=message)
        msg = "Message sent successfully!"
    return render(request, "contact.html", {"msg": msg})


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



class SubjectListCreateAPI(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.get_top_students()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.get_top_students()

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
