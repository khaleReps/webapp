# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, UserSettings, BusinessProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserSettingsForm, BusinessProfileForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Create associated user profile, settings, and business profile
            UserProfile.objects.get_or_create(user=user)
            UserSettings.objects.get_or_create(user=user)
            BusinessProfile.objects.get_or_create(user=user)

            return redirect('webapp:dashboard')

    else:
        form = UserCreationForm()
        user_profile_form = UserProfileForm()
        user_settings_form = UserSettingsForm()
        business_profile_form = BusinessProfileForm()

    return render(request, 'registration/register.html', {
        'form': form,
        'user_profile_form': user_profile_form,
        'user_settings_form': user_settings_form,
        'business_profile_form': business_profile_form,
    })

def profile(request):
    user_id = request.user.id
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)

        if profile_form.is_valid():
            profile_form.save()

    else:
        profile_form = UserProfileForm(instance=user_profile)

    context = {
        'user_profile': user_profile,
        'profile_form': profile_form,
    }

    return render(request, 'webapp/profile.html', context)


@login_required
def settings(request):
    user = request.user.id
    user_profile = UserProfile.objects.get(user=user)
    user_settings = UserSettings.objects.get(user=user)
    business_profile = BusinessProfile.objects.get(user=user)

    if request.method == 'POST':
        user_settings_form = UserSettingsForm(request.POST, instance=user_settings)
        business_profile_form = BusinessProfileForm(request.POST, instance=business_profile)
        
        if user_settings_form.is_valid() and business_profile_form.is_valid():
            user_settings_form.save()
            business_profile_form.save()

    else:
        user_settings_form = UserSettingsForm(instance=user_settings)
        business_profile_form = BusinessProfileForm(instance=business_profile)

    context = {
        'user_profile': user_profile,
        'user_settings': user_settings,
        'business_profile': business_profile,
        'user_settings_form': user_settings_form,
        'business_profile_form': business_profile_form,
    }

    return render(request, 'webapp/settings.html', context)


def search(request):
    query = request.GET.get('q', '')
    results = []
    
    context = {
        'query': query,
        'results': results,
    }
    
    return render(request, 'webapp/search_results.html', context)


@login_required
def business(request):
    user_id = request.user.id
    business_profile = BusinessProfile.objects.get(user=request.user)

    if request.method == 'POST':
        business_profile_form = BusinessProfileForm(request.POST, instance=business_profile)

        if business_profile_form.is_valid():
            business_profile_form.save()

    else:
        business_profile_form = BusinessProfileForm(instance=business_profile)

    context = {
        'business_profile': business_profile,
        'business_profile_form': business_profile_form,
    }

    return render(request, 'webapp/business.html', context)

@login_required
def dashboard(request):
    user_id = request.user.id 
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_settings, created = UserSettings.objects.get_or_create(user=request.user)
    business_profile, created = BusinessProfile.objects.get_or_create(user=request.user)

    context = {
        'user_profile': user_profile, 
        'user_settings': user_settings, 
        'business_profile': business_profile
    }

    return render(request, 'webapp/home.html', context )

