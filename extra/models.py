# models.py
from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.user.username

class College(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=255)

    def __str__(self):
        return self.college_name

from django.db import models

class CollegeTour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='tours/')

    def __str__(self):
        return self.name
