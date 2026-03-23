from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student, Feedback
# Create your views here.

def home(request):
    return render(request, "home.html")

def students(request):
    if request.method == "GET":
        students = Student.objects.all()
        return render(request, "students.html", {"students": students})
    
    elif request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        image = request.FILES.get("image")
        student = Student.objects.create(name=name, age=age, email=email, image=image)
        students = Student.objects.all()
        return render(request, "students.html", {"students": students, 'msg': f"Student {student.name} created successfully!"})
    
def student_delete(request, id):
        student = Student.objects.get(id=id)
        student.delete()
        students = Student.objects.all()
        return redirect("students")

def contact(request):
    if request.method == "GET":
        return render(request, "contact.html")
    
    elif request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        feedback = Feedback.objects.create(email=email, message=message)
        return render(request, "contact.html", {'msg': f"Thank you for your feedback!"})
