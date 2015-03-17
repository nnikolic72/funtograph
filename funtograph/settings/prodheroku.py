from funtograph.settings.base import *

__author__ = 'tanja'

import os
import dj_database_url

#from memcacheify import memcacheify  # @UnresolvedImport
#CACHES = memcacheify()


SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False

TEMPLATE_DEBUG = False
FUNTOGRAPH_IS_LIVE = True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../../static'),
)
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite')
}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
MIDDLEWARE_CLASSES += ('django.middleware.clickjacking.XFrameOptionsMiddleware',)


CLOUDINARY = {
    'cloud_name': os.environ['CLOUDINARY_CLOUD_NAME'],
    'api_key': os.environ['CLOUDINARY_API_KEY'],
    'api_secret': os.environ['CLOUDINARY_API_SECRET'],
    }