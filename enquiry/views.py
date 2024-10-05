from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login
from .forms import StudentSignupForm, CollegeSignupForm
from django.contrib.auth.decorators import login_required

def student_signup_view(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Get or create the 'student' group
            student_group, created = Group.objects.get_or_create(name='student')
            user.groups.add(student_group)  # Add user to 'student' group
            login(request, user)
            return redirect('student_dashboard')  # Redirect to student dashboard
    else:
        form = StudentSignupForm()
    return render(request, 'signup.html', {'form': form, 'user_type': 'Student'})

def college_signup_view(request):
    if request.method == 'POST':
        form = CollegeSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Get or create the 'college' group
            college_group, created = Group.objects.get_or_create(name='college')
            user.groups.add(college_group)  # Add user to 'college' group
            login(request, user)
            return redirect('college_dashboard')  # Redirect to college dashboard
    else:
        form = CollegeSignupForm()
    return render(request, 'signup.html', {'form': form, 'user_type': 'College'})


# Example view for checking user role
def dashboard_view(request):
    if request.user.groups.filter(name='student').exists():
        # User is a student
        return redirect('student_dashboard')
    elif request.user.groups.filter(name='college').exists():
        # User is a college
        return redirect('college_dashboard')



@login_required
def student_dashboard_view(request):
    return render(request, 'dashboard.html', {'user_type': 'Student'})

@login_required
def college_dashboard_view(request):
    return render(request, 'dashboard.html', {'user_type': 'College'})
