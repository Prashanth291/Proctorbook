from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StudentSignupForm

def signup_page(request):
    return render(request, 'templates/student_signup.html', {'form': form})


def home(request):
    return HttpResponse("<h1>Welcome to Proctor Book!</h1>")

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('dashboard')  # Redirect to the student dashboard
    else:
        form = StudentSignupForm()
    
    return render(request, 'student_signup.html', {'form': form})
