from django.urls import path
from .views import HomeView, user_profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView, name='home'),
    path('register/', user_profile_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]