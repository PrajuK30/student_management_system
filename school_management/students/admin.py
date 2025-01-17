from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Class

admin.site.register(Student)  # Register the Student model
admin.site.register(Class)
