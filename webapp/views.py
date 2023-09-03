# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, UserSettings, BusinessProfile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Create associated user profile, settings, and business profile here
            UserProfile.objects.get_or_create(user=user)  # Use get_or_create
            UserSettings.objects.get_or_create(user=user)
            BusinessProfile.objects.get_or_create(user=user)
            return redirect('webapp:dashboard')
            # return redirect('profile')

    else:
           form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)


    context = {
        'user_profile': user_profile, 
        }

    return render(request, 'webapp/profile.html', context )


def settings(request):
    user_settings = UserSettings.objects.get(user=request.user)

    context = {
        'user_settings': user_settings, 
        }

    return render(request, 'webapp/settings.html', context )



def search(request):
    query = request.GET.get('q', '')
    results = []
    
    context = {
        'query': query,
        'results': results,
    }
    
    return render(request, 'webapp/search_results.html', context)



def business(request):
    business_profile = BusinessProfile.objects.get(user=request.user)

    context = {
        'business_profile': business_profile
        }

    return render(request, 'webapp/business.html', context )



def dashboard(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_settings, created = UserSettings.objects.get_or_create(user=request.user)
    business_profile, created = BusinessProfile.objects.get_or_create(user=request.user)

    context = {
        'user_profile': user_profile, 
        'user_settings': user_settings, 
        'business_profile': business_profile
    }

    return render(request, 'webapp/home.html', context )

