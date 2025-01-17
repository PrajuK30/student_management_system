from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache
from .models import Student, Class
from .serializers import StudentSerializer
from django.http import HttpResponse

# API View for getting students (with caching)
@api_view(['GET'])
def get_students(request):
    students = cache.get('students_list')
    if not students:
        students = Student.objects.all()
        cache.set('students_list', students, timeout=60 * 15)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# Home view
def home(request):
    return HttpResponse("Welcome to the School Management System API!")

# View for displaying student list using Django templates
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/students_list.html', {'students': students})

# Add student view
def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        class_assigned = Class.objects.get(id=request.POST['class_assigned'])
        Student.objects.create(name=name, age=age, class_assigned=class_assigned)
        return redirect('student_list')
    classes = Class.objects.all()
    return render(request, 'students/add_student.html', {'classes': classes})

# API View to List Students
class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# API View to Add a New Student
@api_view(['POST'])
def add_student_api(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API View to Update Student Details
@api_view(['PUT'])
def update_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API View to Delete a Student
@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# API View for Specific Student Detail
@api_view(['GET'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

# views.py
def class_list(request):
    classes = Class.objects.all()  # Assuming you have a Class model
    return render(request, 'students/class_list.html', {'classes': classes})

@api_view(['PUT'])
def update_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)  # Get the student by ID
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student, data=request.data)
    
    if serializer.is_valid():
        serializer.save()  # Save the updated student data
        return Response(serializer.data)  # Return the updated student data
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 




