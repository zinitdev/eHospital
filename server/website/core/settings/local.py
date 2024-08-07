from .base import *

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = ["*"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.join(BASE_DIR, 'database'), 'eHospital.sqlite3')
    }
}

INSTALLED_APPS += [
    "debug_toolbar"
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True