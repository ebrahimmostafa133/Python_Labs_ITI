from django.urls import path

from school.views import (
    home, students, student_delete, student_edit, contact,
    subjects, subject_delete, subject_edit,
    grades, grade_delete, grade_edit,
    leaderboard, profile,
    login_view, register_view, logout_view
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("profile/", profile, name="profile"),
    
    path("students/", students, name="students"),
    path("students/<int:id>/delete/", student_delete, name="student_delete"),
    path("students/<int:id>/edit/", student_edit, name="student_edit"),
    
    path("subjects/", subjects, name="subjects"),
    path("subjects/<int:id>/delete/", subject_delete, name="subject_delete"),
    path("subjects/<int:id>/edit/", subject_edit, name="subject_edit"),
    
    path("grades/", grades, name="grades"),
    path("grades/<int:id>/delete/", grade_delete, name="grade_delete"),
    path("grades/<int:id>/edit/", grade_edit, name="grade_edit"),
    
    path("leaderboard/", leaderboard, name="leaderboard"),
]
