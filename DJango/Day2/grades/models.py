from django.db import models

class Grade(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE, related_name='grades')
    value = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.value}"

class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
