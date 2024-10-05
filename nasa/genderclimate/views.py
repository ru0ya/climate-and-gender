from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import UserForm



def home_view(request):
# Example data for counts
    users_count = 500
    doctors_count = 150
    facilities_count = 80
    
    context = {
        'users_count': users_count,
        'doctors_count': doctors_count,
        'facilities_count': facilities_count,
    }

    return render(request, 'home.html', context)


def user_register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # save both User and UserProfile data
            return redirect('login')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})
