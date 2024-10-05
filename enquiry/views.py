# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import StudentSignupForm, CollegeSignupForm
from .models import Student, College

def student_signup_view(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            student_id = form.cleaned_data.get('student_id')
            student = Student.objects.create(user=user, student_id=student_id)

            # Assign the user to the "Student" group
            group, created = Group.objects.get_or_create(name='Student')
            user.groups.add(group)

            login(request, user)
            return redirect('student_dashboard')
    else:
        form = StudentSignupForm()
    
    return render(request, 'signup.html', {'form': form, 'user_type': 'Student'})

def college_signup_view(request):
    if request.method == 'POST':
        form = CollegeSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            college_name = form.cleaned_data.get('college_name')
            college = College.objects.create(user=user, college_name=college_name)

            # Assign the user to the "College" group
            group, created = Group.objects.get_or_create(name='College')
            user.groups.add(group)

            login(request, user)
            return redirect('college_dashboard')
    else:
        form = CollegeSignupForm()

    return render(request, 'signup.html', {'form': form, 'user_type': 'College'})

# Dashboard views
from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard_view(request):
    return render(request, 'dashboard.html', {'user_type': 'Student'})

@login_required
def college_dashboard_view(request):
    return render(request, 'dashboard.html', {'user_type': 'College'})
