
import os

import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['rickycatron.com', 'www.rickycatron.com']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'django_cleanup',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'RickyCatron.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../home/templates')],
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

WSGI_APPLICATION = 'RickyCatron.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

if 'test' in sys.argv:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    STATIC_ROOT = BASE_DIR + '/staticserve'
    MEDIA_ROOT = BASE_DIR + '/mediaserve'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travis',
            'USER': 'postgres',
            'PASSWORD': "",
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.webfaction.com'
    EMAIL_HOST_USER = 'rickycatron'
    EMAIL_HOST_PASSWORD = os.environ['MAIL_PASSWORD']
    EMAIL_PORT = 587
    STATIC_ROOT = '/home/sl33t/webapps/serve/portfolio/static'
    MEDIA_ROOT = '/home/sl33t/webapps/serve/portfolio/media'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'portfolio_db',
            'USER': 'db_admin',
            'PASSWORD': os.environ['DB_PASSWORD'],
            'HOST': 'web518.webfaction.com',
            'PORT': '5432',
        }
    }

# Email settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
DEFAULT_FROM_EMAIL = 'dev@rickycatron.com'
SERVER_EMAIL = 'dev@rickycatron.com'

# Django HTML Validation Settings
HTMLVALIDATOR_ENABLED = True
