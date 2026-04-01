from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q, Sum
from .models import Student, Feedback, Subject, Grade, UserProfile

@login_required
def home(request):
    return render(request, "home.html")


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
