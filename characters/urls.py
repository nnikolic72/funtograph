__author__ = 'tanja'
from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import patterns, url

from .views import (
    CharactersIndexView,
    CharactersPhotographerIndexView
)

urlpatterns = patterns('',
                       url(r'^$', login_required(CharactersIndexView.as_view()), name='index'),
                       url(r'^photographer/(?P<p_photographer_name>.+)/$',
                           login_required(CharactersPhotographerIndexView.as_view()),
                           name='photographer'
                       ),
                       )