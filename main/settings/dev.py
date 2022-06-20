from main.settings.base import INSTALLED_APPS


from .base import *

THIRD_PARTY_APS = [
  'debug_toolbar',
  ]

INSTALLED_APPS += THIRD_PARTY_APS

THIRD_PARTY_MIDDLEWARE = [
  'debug_toolbar.middleware.DebugToolbarMiddleware',
  ]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    
}

INTERNAL_IPS = [
    '127.0.0.1',
]