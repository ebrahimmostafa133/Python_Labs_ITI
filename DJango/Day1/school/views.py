from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q, Sum
from .models import Student, Feedback, Subject, Grade, UserProfile
from .forms import StudentForm, SubjectForm, GradeForm

@login_required
def home(request):
    return render(request, "home.html")

@login_required
def students(request):
    students = Student.objects.all()
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, "students.html", {"students": students, "form": form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    return render(request, "student_form.html", {"form": form})

@login_required
def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect("students")

@login_required
def subjects(request):
    query = request.GET.get('q')
    subjects = Subject.objects.filter(name__icontains=query) if query else Subject.objects.all()
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subject added successfully!")
            return redirect('subjects')
    else:
        form = SubjectForm()
    return render(request, "subjects.html", {"subjects": subjects, "form": form})

@login_required
def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            messages.success(request, "Subject updated successfully!")
            return redirect('subjects')
    else:
        form = SubjectForm(instance=subject)
    return render(request, "subject_form.html", {"form": form})

@login_required
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    messages.success(request, "Subject deleted successfully!")
    return redirect('subjects')

@login_required
def grades(request):
    query = request.GET.get('q')
    grades = Grade.objects.filter(
        Q(student__name__icontains=query) | Q(subject__name__icontains=query)
    ) if query else Grade.objects.all()
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Grade added successfully!")
            return redirect('grades')
    else:
        form = GradeForm()
    return render(request, "grades.html", {"grades": grades, "form": form})

@login_required
def grade_update(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            messages.success(request, "Grade updated successfully!")
            return redirect('grades')
    else:
        form = GradeForm(instance=grade)
    return render(request, "grade_form.html", {"form": form})

@login_required
def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    grade.delete()
    messages.success(request, "Grade deleted successfully!")
    return redirect('grades')

@login_required
def userprofile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, "userprofile.html", {"profile": profile})

@login_required
def leaderboard(request):
    top_students = Student.objects.annotate(total=Sum('grade__grade_value')).order_by('-total')[:5]
    return render(request, "leaderboard.html", {"top_students": top_students})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

def contact(request):
    if request.method == "GET":
        return render(request, "contact.html")
    
    elif request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(email=email, message=message)
        return render(request, "contact.html", {'msg': f"Thank you for your feedback!"})
