from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Set password
            user.set_password(form.cleaned_data['password'])
            user.save()
            #messages.success(request, 'Registration successful.')
            # Handle successful registration (e.g., send welcome email, redirect)
            return redirect('login')  # Replace with your desired redirect URL
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,  password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace with your desired redirect URL
            else:
                # Invalid credentials
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})  

def user_logout(request):
    logout(request)
    return redirect('home') 
def start_page(request):
    return render(request, 'start.html')
@login_required
def home(request):
    return render(request, 'home.html')
