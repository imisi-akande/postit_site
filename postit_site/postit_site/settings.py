"""
Django settings for postit_site project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dotenv
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = dotenv.get('SECRET', 'ifewioifr')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = dotenv.get('DEBUG', False)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'comments',
    'users',
    'rest_framework',
    'postit',
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'postit_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'postit_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    } if DEBUG else dj_database_url.config()
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )    
}

'''
curl -X POST -d "username=jed&password=password123" http://127.0.0.1:8000/api/auth/token/
"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1LCJ1c2VybmFtZSI6ImplZCIsImV4cCI6MTUwMDkzODk5MywiZW1haWwiOiJqZWRAeWFob28uY29tIn0.5NtWU9VV7nMRjKG7Xe5wLs2O2q3HH5R9noyRSQPraEs"
 
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1LCJ1c2VybmFtZSI6ImplZCIsImV4cCI6MTUwMDkzODk5MywiZW1haWwiOiJqZWRAeWFob28uY29tIn0.5NtWU9VV7nMRjKG7Xe5wLs2O2q3HH5R9noyRSQPraEs" http://127.0.0.1:8000/api/comments/

curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1LCJ1c2VybmFtZSI6ImplZCIsImV4cCI6MTUwMDk0MDMyMSwiZW1haWwiOiJqZWRAeWFob28uY29tIn0.xgf34GJ6DpMurTdF60-yYbF-ihf-YgXdbc0Na2RElmY" -H "Content-Type: application/json" -d '{"content":"Be Prepared"}' http://127.0.0.1:8000/api/comments/create/?slug=data-science&type=post


curl -X POST -H "Authorization: JWT  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo1LCJ1c2VybmFtZSI6ImplZCIsImV4cCI6MTUwMDk0MDMyMSwiZW1haWwiOiJqZWRAeWFob28uY29tIn0.xgf34GJ6DpMurTdF60-yYbF-ihf-YgXdbc0Na2RElmY._i5wEqJ_OO8wNiVVNAWNPGjGaO7OzChY0UzONgw06D0
" -H "Content-Type: application/json" -d '{"content”:”This is interesting”}’ 'http://127.0.0.1:8000/api/comments/create/?slug=new-title&type=post&parent_id=3' 

'''










