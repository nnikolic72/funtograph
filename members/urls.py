

__author__ = 'n.nikolic'

from django.conf.urls import patterns, url

from .views import (
    MemberHomePageView,
    MemberRegisterView,
    MemberLoginView,
    MemberWelcomeView,
    MemberDashboardView,
)
__author__ = 'n.nikolic'

urlpatterns = patterns('',
    url(r'^$', MemberHomePageView.as_view(), name='index'),
    url(r'^register/$', MemberRegisterView.as_view(), name='register'),
    url(r'^login/$', MemberLoginView.as_view(), name='login'),
    url(r'^welcome/$', MemberWelcomeView.as_view(), name='welcome'),
    url(r'^dashboard/$', MemberDashboardView.as_view(), name='dashboard'),
)