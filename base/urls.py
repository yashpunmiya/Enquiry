"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from enquiry import views

urlpatterns = [
    path('signup/student/', views.student_signup_view, name='student_signup'),
    path('signup/college/', views.college_signup_view, name='college_signup'),
    path('dashboard/student/', views.student_dashboard_view, name='student_dashboard'),
    path('dashboard/college/', views.college_dashboard_view, name='college_dashboard'),
    path('tour/<int:tour_id>/', views.college_tour, name='college_tour'),
    
]
