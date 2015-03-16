from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from .views import (PhotosUploadView,
                    MembersPhotosView
)

__author__ = 'n.nikolic'

urlpatterns = patterns('',
                       url(r'^upload/$', login_required(PhotosUploadView.as_view()), name='upload'),
                       url(r'^photographer/(?P<p_photographer_name>.+)/$',
                           login_required(MembersPhotosView.as_view()),
                           name='photographer'
                       ),
                       )