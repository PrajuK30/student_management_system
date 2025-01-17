from django.db import models

# Create your models here.
from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.section}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

