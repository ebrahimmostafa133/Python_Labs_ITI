from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics

from .models import Subject
from .serializers import SubjectSerializer

"""
@login_required
def subjects_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        Subject.objects.create(name=name, description=description)
        return redirect("subjects")
    subjects = Subject.objects.all()
    return render(request, "subjects/subjects.html", {"subjects": subjects})

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
    return render(request, "subjects/subject_edit.html", {"subject": subject})
"""

class SubjectListCreateAPI(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
