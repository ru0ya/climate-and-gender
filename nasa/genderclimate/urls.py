from django.urls import path
from .views import HomeView, user_profile_view

urlpatterns = [
    path('', HomeView, name='home'),
    path('register', user_profile_view, name='register'),
]