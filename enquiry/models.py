from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=10)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class CollegeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=255)
    college_code = models.CharField(max_length=10)

    def __str__(self):
        return self.college_name
