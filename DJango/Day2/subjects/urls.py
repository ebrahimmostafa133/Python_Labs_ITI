from django.urls import path
from . import views

urlpatterns = [
    # path('subjects_list/', views.subjects_view, name='subjects'),
    # path('subjects/edit/<int:pk>/', views.subject_edit, name='subject_edit'),
    # path('subjects/delete/<int:pk>/', views.subject_delete, name='subject_delete'),
    
    # API
    path('api/subjects/', views.SubjectListCreateAPI.as_view(), name='subject-api-list'),
    path('api/subjects/<int:pk>/', views.SubjectDetailAPI.as_view(), name='subject-api-detail'),
]
