from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

def HomeView(request):
    return render(request, 'home.html')


def user_register_view(request):
    if request.method == 'POST':
        form =UserProfileForm(request.POST)
        if form.is_valid():
            form.save()  #save both User and UserProfile data
            return redirect('login')
    else:
        form = UserProfileForm()

    return render(request, 'register.html', {'form': form})