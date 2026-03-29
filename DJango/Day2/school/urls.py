from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'grades', views.GradeViewSet, basename='grade')
router.register(r'feedback', views.FeedbackViewSet, basename='feedback')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')
router.register(r'profiles', views.UserProfileViewSet, basename='profile')

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    
    path('students/', views.students_view, name='students'),
    path('students/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),
    
    path('subjects/', views.subjects_view, name='subjects'),
    path('subjects/edit/<int:pk>/', views.subject_edit, name='subject_edit'),
    path('subjects/delete/<int:pk>/', views.subject_delete, name='subject_delete'),
    
    path('grades/', views.grades_view, name='grades'),
    path('grades/edit/<int:pk>/', views.grade_edit, name='grade_edit'),
    path('grades/delete/<int:pk>/', views.grade_delete, name='grade_delete'),
    
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('contact/', views.contact_view, name='contact'),

    # API Endpoints
    path('api/students/', views.student_api_list, name='student-api-list'),
    path('api/students/<int:pk>/', views.student_api_detail, name='student-api-detail'),
    path('api/subjects/', views.SubjectListCreateAPI.as_view(), name='subject-api-list'),
    path('api/subjects/<int:pk>/', views.SubjectDetailAPI.as_view(), name='subject-api-detail'),
    path('api/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls')),
]
