from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to="students/")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
