from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="students/")
    date_added = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_top_students(limit=5):
        from django.db.models import Sum
        return Student.objects.annotate(total=Sum("grades__value")).order_by("-total")[:limit]

    def __str__(self):
        return self.name
