import os

from .base import *

from dotenv import dotenv_values


print('local')

config = dotenv_values()

SECRET_KEY = config.get("DJANGO_SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = config.get("INTERNAL_IPS")

INSTALLED_APPS += ['debug_toolbar',]
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.get("POSTGRES_DB"),
        "USER": config.get("POSTGRES_USER"),
        "PASSWORD": config.get("POSTGRES_PASSWORD"),
        "HOST": config.get("POSTGRES_HOST"),
        "PORT": config.get("POSTGRES_PORT"),
    },
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = BASE_DIR / 'media'
