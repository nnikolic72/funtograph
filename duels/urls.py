__author__ = 'n.nikolic'
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from .views import (
    PhotoDuelsView,
    PhotoDuelsChallengeView,
)

urlpatterns = patterns('',
                       url(r'^$', login_required(PhotoDuelsView.as_view()), name='index'),
                       url(r'^duelchallenge/(?P<p_photo_id>.+)/$',
                           login_required(PhotoDuelsChallengeView.as_view()),
                           name='duelchallenge'
                       ),
                       )