from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'grades', views.GradeViewSet, basename='grade')

urlpatterns = [
    path("", views.home, name="home"),
    
    path('students/', views.student_api_list, name='student-list'),
    path('students/<int:pk>/', views.student_api_detail, name='student-detail'),
    
    path('subjects/', views.SubjectListCreateAPI.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', views.SubjectDetailAPI.as_view(), name='subject-detail'),
    
    path('', include(router.urls)),
    
    path('leaderboard/', views.leaderboard_api, name='leaderboard-api'),

    path('api-auth/', include('rest_framework.urls')),
]
