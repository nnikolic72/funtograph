

__author__ = 'n.nikolic'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from .views import (
    MemberHomePageView,
    MemberRegisterView,
    MemberLoginView,
    MemberWelcomeView,
    MemberDashboardView,
    MemberDisabledView,
    MemberLogoutView
)
__author__ = 'n.nikolic'

urlpatterns = patterns('',
    #url(r'^$', login_required(MemberHomePageView.as_view()), name='index'),
    url(r'^register/$', MemberRegisterView.as_view(), name='register'),
    url(r'^login/$', MemberLoginView.as_view(), name='login'),
    url(r'^welcome/$', login_required(MemberWelcomeView.as_view()), name='welcome'),
    url(r'^dashboard/$', login_required(MemberDashboardView.as_view()), name='dashboard'),
    url(r'^disabled/$', MemberDisabledView.as_view(), name='disabled'),
    url(r'^logout/$', login_required(MemberLogoutView.as_view()), name='logout'),
)