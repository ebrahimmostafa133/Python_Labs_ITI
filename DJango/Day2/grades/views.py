from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from .models import Grade, Feedback
from students.models import Student
from subjects.models import Subject
from .serializers import GradeSerializer, FeedbackSerializer

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
        "grades/grades.html",
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
        "grades/grade_edit.html",
        {"grade": grade, "students": students, "subjects": subjects},
    )

def contact_view(request):
    msg = None
    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        Feedback.objects.create(email=email, message=message)
        msg = "Message sent successfully!"
    return render(request, "grades/contact.html", {"msg": msg})

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
