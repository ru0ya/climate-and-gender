from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home_view, user_register_view


urlpatterns = [
    path('', home_view, name='home'),
    path('register/', user_register_view, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
