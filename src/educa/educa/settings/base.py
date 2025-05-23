from pathlib import Path

from django.urls import reverse_lazy

# from pythonjsonlogger.json import JsonFormatter

# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent.parent # если не файл, а папка settings

INSTALLED_APPS = [
    'daphne',
    'students.apps.StudentsConfig',
    'courses.apps.CoursesConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.postgres',
    'embed_video',
    'redisboard',
    'rest_framework',
    'channels',

    'chat.apps.ChatConfig',
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

ROOT_URLCONF = 'educa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'educa.wsgi.application'
ASGI_APPLICATION = 'educa.asgi.application' 

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

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = reverse_lazy('student_course_list')

# django rest framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# # logs
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,

#     'formatters': {
#         'formatter':{
#             'format': '{levelname} {asctime} {filename} {message}',
#             'style': '{', 
#             },
#         'server_formatter': {
#             '()': 'django.utils.log.ServerFormatter',
#             'format': '{levelname} {asctime} {filename} {message}',
#             'style': '{',
#             },
#         'json_formatter': {
#             '()': JsonFormatter,
#             'format': '{levelname} {asctime} {filename} {message}',
#             'style': '{',
#             }
#         },
#     'handlers': {
#         'file': {
#             'level': 'WARNING',
#             'class': 'logging.FileHandler',
#             'filename': 'log.log',
#             'formatter': 'server_formatter',
#             'encoding': 'UTF-8'
#             },
#         'json_file': {
#             'level': 'WARNING',
#             'class': 'logging.FileHandler',
#             'filename': 'log.json',
#             'formatter': 'json_formatter',
#             'encoding': 'UTF-8'
#             },
#         },
#     'loggers': {
#         'reserv': {
#             'handlers': ['file', 'json_file'],
#             'level': 'WARNING',
#             'propagate': True,
#             },
#         },
#     }
