from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Use this function to get the custom user model
User = get_user_model()

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup')

        # Create the new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Log the user in and redirect to home
        login(request, user)
        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')

@login_required  
def home(request):
    return render(request, 'home.html')