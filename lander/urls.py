from django.conf.urls import patterns, url

from .views import LanderHomePageView
__author__ = 'n.nikolic'

urlpatterns = patterns('',
    url(r'^$', LanderHomePageView.as_view(), name = 'index'),
)