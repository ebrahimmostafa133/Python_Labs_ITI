from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Sum

from .models import Student, Subject, Grade, Feedback

@login_required
def home(request):
    return render(request, "home.html")

@login_required
def students(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        image = request.FILES.get("image")
        Student.objects.create(name=name, age=age, email=email, image=image)
        return redirect("students")

    student_list = Student.objects.all()
    return render(request, "students.html", {"students": student_list})

@login_required
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("students")

@login_required
def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.email = request.POST.get("email")
        if request.FILES.get("image"):
            student.image = request.FILES.get("image")
        student.save()
        return redirect("students")
    return render(request, "student_edit.html", {"student": student})

@login_required
def subjects(request):
    query = request.GET.get("q", "")
    subjects_qs = Subject.objects.all()
    if query:
        subjects_qs = subjects_qs.filter(name__icontains=query)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        Subject.objects.get_or_create(name=name, defaults={"description": description})
        return redirect("subjects")

    return render(request, "subjects.html", {"subjects": subjects_qs, "query": query})

@login_required
def subject_delete(request, id):
    sub = get_object_or_404(Subject, id=id)
    sub.delete()
    return redirect("subjects")

@login_required
def subject_edit(request, id):
    sub = get_object_or_404(Subject, id=id)
    if request.method == "POST":
        sub.name = request.POST.get("name")
        sub.description = request.POST.get("description")
        sub.save()
        return redirect("subjects")
    return render(request, "subject_edit.html", {"subject": sub})

@login_required
def grades(request):
    student_filter = request.GET.get("student_id")
    subject_filter = request.GET.get("subject_name")

    grades_qs = Grade.objects.select_related("student", "subject").all()
    if student_filter:
        grades_qs = grades_qs.filter(student__id=student_filter)
    if subject_filter:
        grades_qs = grades_qs.filter(subject__name__icontains=subject_filter)

    if request.method == "POST":
        student_id = request.POST.get("student")
        subject_id = request.POST.get("subject")
        value = float(request.POST.get("value") or 0)
        student = get_object_or_404(Student, id=student_id)
        subject = get_object_or_404(Subject, id=subject_id)
        Grade.objects.update_or_create(student=student, subject=subject, defaults={"value": value})
        return redirect("grades")

    return render(request, "grades.html", {
        "grades": grades_qs,
        "students": Student.objects.all(),
        "subjects": Subject.objects.all(),
        "student_filter": student_filter,
        "subject_filter": subject_filter,
    })

@login_required
def grade_delete(request, id):
    grade = get_object_or_404(Grade, id=id)
    grade.delete()
    return redirect("grades")

@login_required
def grade_edit(request, id):
    grade = get_object_or_404(Grade, id=id)
    if request.method == "POST":
        grade.value = float(request.POST.get("value") or 0)
        grade.save()
        return redirect("grades")
    return render(request, "grade_edit.html", {"grade": grade})

@login_required
def leaderboard(request):
    top_students = (
        Student.objects.annotate(total=Sum("grades__value"))
        .order_by("-total")[:5]
    )
    return render(request, "leaderboard.html", {"top_students": top_students})

@login_required
def profile(request):
    return render(request, "userProfile.html")

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

def contact(request):
    if request.method == "GET":
        return render(request, "contact.html")
    
    elif request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        Feedback.objects.create(email=email, message=message)
        return render(request, "contact.html", {'msg': f"Thank you for your feedback!"})
