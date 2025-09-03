from django.urls import path
from . import views
from . import views_api

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('exam/create/', views.exam_create, name='exam_create'),
    path('exam/<int:exam_id>/question/add/', views.question_create, name='question_create'),

     path('api/exams/', views_api.api_exams, name='api_exams'),
    path('api/exams/<int:exam_id>/', views_api.api_exam_detail, name='api_exam_detail'),
    path('api/exams/<int:exam_id>/questions/', views_api.api_question_create, name='api_question_create'),
    path('demo/', views.api_demo, name='api_demo'),
]
