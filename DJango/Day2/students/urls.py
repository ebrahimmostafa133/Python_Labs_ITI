from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')
router.register(r'profiles', views.UserProfileViewSet, basename='profile')

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path('students_list/', views.students_view, name='students'), # Changed to avoid collision if mounted at same level
    path('students/edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('leaderboard_view/', views.leaderboard_view, name='leaderboard'),
    
    # API
    path('api/students/', views.student_api_list, name='student-api-list'),
    path('api/students/<int:pk>/', views.student_api_detail, name='student-api-detail'),
    path('api/', include(router.urls)),
]
