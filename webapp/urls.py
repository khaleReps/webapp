from django.urls import path, include  
from django.contrib.auth import views as auth_views  
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('register/', views.register, name='register'),

    # Include authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='webapp/login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(next_page='webapp:register'), name='logout'),    

    path('search/', views.search, name='search'),

    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('business/', views.business, name='business'),
]
