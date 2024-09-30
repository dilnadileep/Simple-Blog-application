from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login 
from .models import CustomUser  # Assuming you're using CustomUser model
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import BlogPost


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


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Use renamed login function
            return redirect('home')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')

@login_required  
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        user = request.user
        user.username = username
        user.email = email
        user.save()

        messages.success(request, 'Your profile has been updated successfully!')
        return redirect('profile')

    return render(request, 'profile.html')





@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        # Validate fields
        if not title or not content:
            error_message = "All fields are required."
            return render(request, 'create_post.html', {'error_message': error_message})
        
        # Create the blog post
        blog_post = BlogPost(title=title, content=content, author=request.user)
        blog_post.save()
        return redirect('home')  # Redirect after creating the post
    return render(request, 'create_post.html')



# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from django.core.paginator import Paginator

# View all posts with pagination
@login_required
def view_posts(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'view_posts.html', {'page_obj': page_obj})

# View a single post
@login_required
def view_single_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'view_single_post.html', {'post': post})

# Update a post
@login_required
def update_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('view_posts')
    return render(request, 'update_post.html', {'post': post})

# Delete a post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('view_posts')
    return render(request, 'delete_post.html', {'post': post})


# app/views.py
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
