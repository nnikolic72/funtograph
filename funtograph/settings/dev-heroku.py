from funtograph.settings import base

__author__ = 'tanja'

import os
import dj_database_url

#from memcacheify import memcacheify  # @UnresolvedImport
#CACHES = memcacheify()


SECRET_KEY =  os.environ['SECRET_KEY']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    base.os.path.join(base.BASE_DIR, '../../static'),
)
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite')
}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
base.MIDDLEWARE_CLASSES += ('django.middleware.clickjacking.XFrameOptionsMiddleware',)
