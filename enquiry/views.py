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













import os
from dotenv import load_dotenv
from django.shortcuts import render
import genai

# Load the environment variables (for API keys)
load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Predefined College Data for Engineering Colleges in Mumbai
college_data = [
    {
        "marks_range": [90, 100],
        "location": "Mumbai",
        "course": "Engineering",
        "budget_range": [100000, 500000],
        "suggestions": [
            "1. IIT Bombay: Top-tier placements and great facilities.",
            "2. VJTI Mumbai: Excellent reviews with consistent placements.",
            "3. SPIT: Located in Andheri, good for engineering students."
        ]
    },
    {
        "marks_range": [85, 90],
        "location": "Mumbai",
        "course": "Engineering",
        "budget_range": [100000, 500000],
        "suggestions": [
            "1. KJ Somaiya: Excellent placements and strong faculty.",
            "2. DJ Sanghvi: Well-known for tech and engineering courses.",
            "3. Thadomal Shahani Engineering College: Affordable with great reviews."
        ]
    },
    # Additional colleges can be added here...
]

def get_college_recommendations(marks, location, course, budget):
    """ Fetch college recommendations from pre-defined college data. """
    for data in college_data:
        if data["marks_range"][0] <= marks <= data["marks_range"][1] and \
           "mumbai" in location.lower() and \
           data["course"].lower() == course.lower() and \
           data["budget_range"][0] <= budget <= data["budget_range"][1]:
            return "\n".join(data["suggestions"])
    return "No exact matches found. Try adjusting your filters."

def college_recommendation(request):
    response_text = ""
    if request.method == "POST":
        student_name = request.POST.get("student_name", "")
        marks = int(request.POST.get("marks", ""))
        address = request.POST.get("address", "")
        location = request.POST.get("location", "")
        course = request.POST.get("course", "")
        budget = int(request.POST.get("budget", ""))
        special_requirements = request.POST.get("special_requirements", "")

        # Process latitude, longitude if provided for current location
        if "," in location:
            lat, lon = map(float, location.split(","))
            # Example: find the closest college based on lat/lon (pseudo-code)
            location = "Mumbai"  # Simulating for now

        # Fetch recommendations from pre-defined data
        college_suggestions = get_college_recommendations(marks, location, course, budget)
        
        if not college_suggestions:
            # Fallback to AI model if no pre-defined matches (optional)
            user_input = f"""
            Suggest engineering colleges in Mumbai for a student with:
            Name: {student_name}
            Marks: {marks}
            Address: {address}
            Location: {location}
            Course: {course}
            Budget: {budget}
            Special Requirements: {special_requirements}
            """

            model = genai.GenerativeModel(
                model_name="gemini-1.0-pro",
                generation_config=generation_config,
            )

            chat_session = model.start_chat(history=[])
            response = chat_session.send_message(user_input)
            response_text = response.text
        else:
            response_text = college_suggestions

    context = {'response': response_text}
    return render(request, 'gemini.html', context)
