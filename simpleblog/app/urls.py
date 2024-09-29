from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView


urlpatterns = [
#    path('', views.index, name="index"),
   path('',views.signup, name='signup'),
   path('login/', views.login_view, name='login'),
   path('home/', views.home, name='home'),
   path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout view with redirect to login




]
