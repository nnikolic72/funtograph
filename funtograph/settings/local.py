from unipath import Path
from funtograph.settings.base import *

__author__ = 'tanja'

from ConfigParser import ConfigParser

DEBUG = True
ALLOWED_HOSTS = ['*']


TEMPLATE_DEBUG = True


#FUNTOGRAPH_IS_LIVE = True

config = ConfigParser()
settings_path = PROJECT_DIR.child('funtograph').child("settings")
settings_path = Path(settings_path, 'settings.ini')
config.read(settings_path)

SECRET_KEY =  config.get('funtograph', 'APP_SECRET_KEY')
DATABASE_USER = config.get('database', 'DATABASE_USER')
DATABASE_PASSWORD = config.get('database', 'DATABASE_PASSWORD')
DATABASE_HOST = config.get('database', 'DATABASE_HOST')
DATABASE_PORT = config.get('database', 'DATABASE_PORT')
DATABASE_ENGINE = config.get('database', 'DATABASE_ENGINE')
DATABASE_NAME = config.get('database', 'DATABASE_NAME')

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_ROOT = PROJECT_DIR.child("static")
MEDIA_URL = '/media/'
STATICFILES_DIRS = (
    PROJECT_DIR.child("assets"),
)

#  Cloudinary settings
# Cloudinary settings for Django. Add to your settings file.
CLOUDINARY = {
    'cloud_name': config.get('cloudinary', 'CLOUDINARY_CLOUD_NAME'),
    'api_key': config.get('cloudinary', 'CLOUDINARY_API_KEY'),
    'api_secret': config.get('cloudinary', 'CLOUDINARY_SECRET_KEY'),
    }

import cloudinary
cloudinary.config(
  cloud_name = CLOUDINARY['cloud_name'],
  api_key = CLOUDINARY['api_key'],
  api_secret = CLOUDINARY['api_secret']
)


