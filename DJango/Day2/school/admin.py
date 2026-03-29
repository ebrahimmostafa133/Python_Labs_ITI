from django.contrib import admin
from .models import Student, Feedback, UserProfile

# Register your models here.

admin.site.register(Student)
admin.site.register(Feedback)
admin.site.register(UserProfile)
