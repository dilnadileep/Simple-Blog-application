from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView
from .views import BlogPostListCreate, BlogPostRetrieveUpdateDestroy


urlpatterns = [
#    path('', views.index, name="index"),
   path('',views.signup, name='signup'),
   path('login/', views.login, name='login'),
   path('home/', views.home, name='home'),
   path('logout/', views.logout_view, name='logout'),
   path('profile/', views.profile, name='profile'),  
   path('create-post/', views.create_post, name='create_post'),
   path('view-posts/', views.view_posts, name='view_posts'),  
   path('post/<int:post_id>/', views.view_single_post, name='view_single_post'),  
   path('post/update/<int:post_id>/', views.update_post, name='update_post'),  
   path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),  
   path('api/posts/', BlogPostListCreate.as_view(), name='post-list-create'),
   path('api/posts/<int:pk>/', BlogPostRetrieveUpdateDestroy.as_view(), name='post-detail'),


   




]
