from django.urls import path
from . import views

urlpatterns = [
    # Home view
    path('', views.student_list, name='student_list'),  # Map /students/ to student_list view

    # Template views
    path('add/', views.add_student, name='add_student'),  # Add student form

    # API views
    path('api/students/', views.StudentList.as_view(), name='api_student_list'),  # List students (API)
    path('api/students/add/', views.add_student_api, name='api_add_student'),  # Add a new student (API)
    path('api/students/<int:pk>/update/', views.update_student, name='api_update_student'),  # Update student (API)
    path('api/students/<int:pk>/delete/', views.delete_student, name='api_delete_student'),  # Delete student (API)
    path('api/students/<int:pk>/', views.student_detail, name='api_student_detail'),  # Student detail (API)
    path('api/', views.get_students, name='get_students'),  # API for cached students
    path('class/', views.class_list, name='class_list'),  # URL for /class/
   
   
   
      

]











