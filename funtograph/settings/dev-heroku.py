__author__ = 'tanja'

import os
import dj_database_url  # @UnresolvedImport

#from memcacheify import memcacheify  # @UnresolvedImport
#CACHES = memcacheify()

from funtograph.settings.base import * # @UnusedWildImport

config = ConfigParser()
settings_path = PROJECT_DIR.child('funtograph').child("settings")
settings_path = Path(settings_path, 'settings.ini')
config.read(settings_path)

SECRET_KEY =  config.get('funtograph', 'API_SECRET_KEY')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../../static'),
)
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite')
}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
MIDDLEWARE_CLASSES += ('django.middleware.clickjacking.XFrameOptionsMiddleware',)
