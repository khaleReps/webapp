# Webapp

Webapp is a Django application designed as a starting point for user-based projects.

## Prerequisites

Before getting started, make sure you have a superuser profile created for your Django project.

## Installation

1. Download the `webapp` project and install its requirements using pip:

`pip install -r requirements.txt`


2. Place the `webapp` folder in your project directory, alongside your SQL file.

3. Include the `webapp` app in your project's `settings.py` by adding it to the `INSTALLED_APPS` list:

`
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Packages
    'djmoney',
    'django_countries',

    # Custom Apps
    'webapp',
]
`

LOGIN_REDIRECT_URL = 'webapp:login'



Include the webapp app in your project's urls.py:
`
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
`

Run migrations to create the database tables:
`django-admin makemigrations && django-admin migrate`

You're all set! Now, start the server by running the following command:
`python manage.py runserver`


###Usage

Visit the Django admin panel at http://localhost:8000/admin/ and start building your user-based project with Webapp.

###Author
Built by KS Tsoaela