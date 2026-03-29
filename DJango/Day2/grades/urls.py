from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'grades', views.GradeViewSet, basename='grade')
router.register(r'feedback', views.FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('grades_list/', views.grades_view, name='grades'),
    path('grades/edit/<int:pk>/', views.grade_edit, name='grade_edit'),
    path('grades/delete/<int:pk>/', views.grade_delete, name='grade_delete'),
    path('contact_view/', views.contact_view, name='contact'),
    path('api/', include(router.urls)),
]
