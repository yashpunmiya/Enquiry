from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/student/', views.student_dashboard_view, name='student_dashboard'),  # Ensure the name is 'student_dashboard'
    path('dashboard/college/', views.college_dashboard_view, name='college_dashboard'),
    path('signup/student/', views.student_signup_view, name='student_signup'),
    path('signup/college/', views.college_signup_view, name='college_signup'),
    path('college-recommendation/', views.college_recommendation, name='college_recommendation'),
]
