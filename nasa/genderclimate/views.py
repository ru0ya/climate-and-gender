from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import UserForm


def HomeView(request):
    return render(request, 'home.html')


def user_register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # save both User and UserProfile data
            return redirect('login')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'home.html', {'form': form})
