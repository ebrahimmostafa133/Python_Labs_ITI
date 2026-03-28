"""
URL configuration for iti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import home, students, student_update, student_delete, subjects, subject_update, subject_delete, grades, grade_update, grade_delete, userprofile, leaderboard, login_view, logout_view, contact

urlpatterns = [
    path("", login_view, name="login"),
    path("home/", home, name="home"),
    path("students/", students, name="students"),
    path("students/<int:pk>/update/", student_update, name="student_update"),
    path("student_delete/<int:id>/", student_delete, name="student_delete"),
    path("subjects/", subjects, name="subjects"),
    path("subjects/<int:pk>/update/", subject_update, name="subject_update"),
    path("subjects/<int:pk>/delete/", subject_delete, name="subject_delete"),
    path("grades/", grades, name="grades"),
    path("grades/<int:pk>/update/", grade_update, name="grade_update"),
    path("grades/<int:pk>/delete/", grade_delete, name="grade_delete"),
    path("userprofile/", userprofile, name="userprofile"),
    path("leaderboard/", leaderboard, name="leaderboard"),
    path("logout/", logout_view, name="logout"),
    path("contact/", contact, name="contact"),
]
