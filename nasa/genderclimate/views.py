from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm

def HomeView(request):
    return render(request, 'home.html')

@login_required
def user_profile_view(request):
    # Check if the user already has a profile
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        if profile:
            # If the user has a profile, update it
            form = UserProfileForm(request.POST, instance=profile)
        else:
            # If the user doesn't have a profile, create a new one
            form = UserProfileForm(request.POST)
        
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Assign the user to the profile
            user_profile.save()
            # return redirect('profile_success')  # Redirect to a success page or the user dashboard
    else:
        if profile:
            # Populate the form with the existing profile information
            form = UserProfileForm(instance=profile)
        else:
            # Empty form for creating a new profile
            form = UserProfileForm()

    return render(request, 'register.html', {'form': form})