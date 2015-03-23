__author__ = 'n.nikolic'
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from .views import PhotoDuelsView

urlpatterns = patterns('',
                       url(r'^$', login_required(PhotoDuelsView.as_view()), name='index'),
                       )