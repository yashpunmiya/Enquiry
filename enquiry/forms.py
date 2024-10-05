# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, College

class StudentSignupForm(UserCreationForm):
    student_id = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CollegeSignupForm(UserCreationForm):
    college_name = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
