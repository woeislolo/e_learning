import os

from .base import *

from dotenv import dotenv_values


print('local')

config = dotenv_values()

SECRET_KEY = config.get("DJANGO_SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ["*"]

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

# уточнит про статику и медиал - что в локал. что в прорд
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_ROOT = BASE_DIR / 'media'
