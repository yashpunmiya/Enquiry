from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentProfile, CollegeProfile

class StudentSignupForm(UserCreationForm):
    roll_number = forms.CharField(max_length=10)
    course = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create the student's profile
            student_profile = StudentProfile.objects.create(
                user=user,
                roll_number=self.cleaned_data['roll_number'],
                course=self.cleaned_data['course']
            )
        return user

class CollegeSignupForm(UserCreationForm):
    college_name = forms.CharField(max_length=255)
    college_code = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create the college's profile
            college_profile = CollegeProfile.objects.create(
                user=user,
                college_name=self.cleaned_data['college_name'],
                college_code=self.cleaned_data['college_code']
            )
        return user
