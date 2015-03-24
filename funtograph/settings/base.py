__author__ = 'tanja'

"""
Django settings for funtograph project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


import os
from unipath import Path
from ConfigParser import ConfigParser

#this is overriden in other config files
FUNTOGRAPH_IS_LIVE = True
try:
    if os.environ['FUNTOGRAPH_IS_LIVE']:
        FUNTOGRAPH_IS_LIVE = os.environ['FUNTOGRAPH_IS_LIVE']
except:
    pass

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-14845987-3'
GOOGLE_ANALYTICS_DOMAIN = 'funtograph.com'

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = Path(__file__).ancestor(3)
BASE_DIR = PROJECT_DIR.child('funtograph')


config = ConfigParser()
settings_path = PROJECT_DIR.child('funtograph').child("settings")
settings_path = Path(settings_path, 'settings.ini')
config.read(settings_path)

TEMPLATE_DIRS = (
    PROJECT_DIR.child("templates"),
    PROJECT_DIR.child("templates").child("funtograph"),
                 )

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'funtograph.context-processors.google_analytics',
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap3',
    'cloudinary',
    'dajaxice',


    'lander',
    'members',
    'characters',
    'photos',
    'interactions',
    'duels',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'funtograph.urls'

WSGI_APPLICATION = 'funtograph.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

#Set this to True to include language selectors
SHOW_TRANSLATIONS = False

LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'es'

LANGUAGES = (
    ('en', 'English'),
    ('de', 'German'),
    ('es', 'Spanish'),
)

#LOCALE_DIR = PROJECT_DIR.child("locale")

LOCALE_PATHS = (
    PROJECT_DIR.child("locale"),

)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)

STATIC_URL = '/static/'

LOGIN_URL = '/members/login'
LOGOUT_URL = '/members/logout'
LOGIN_REDIRECT_URL = '/members/dashboard'

# Funtograph default preferences
MAX_UPLOAD_PHOTOS_DEFAULT = 5  # How many max photos user can upload to Funtograph
INITIAL_PHOTO_DUELS_TO_DISPLAY = 5  # How many duels to display on PhotoDuels index page

INTERACTION_LIKE_WEIGHT = 1
INTERACTION_DISLIKE_WEIGHT = -1
INTERACTION_FAVORITE_WEIGHT = 5
INTERACTION_DUEL_WIN_WEIGHT = 10
INTERACTION_DUEL_LOSS_WEIGHT = -5



