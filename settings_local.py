import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = 'django-insecure-8t%_ab*1d$igbg+dkm+5g&odj%ei5j)7m8h6iq!s41y7i^$q3d'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_HOST_USER = 'iqworks@bk.ru'
EMAIL_HOST_PASSWORD = 'fQJqjUNCn5J17e61bBAF'
