from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponseRedirect
from funtograph.settings.base import STATIC_URL

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),  # go to /i18n/setlang/
    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(STATIC_URL+'ico/favicon.ico')), #google chrome favicon fix
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    url(r'^', include('lander.urls', namespace='lander')),
    url(r'^members/', include('members.urls', namespace='members')),
    url(r'^photos/', include('photos.urls', namespace='photos')),
    url(r'^characters/', include('characters.urls', namespace='characters')),
    url(r'^duels/', include('duels.urls', namespace='duels')),
)

urlpatterns += staticfiles_urlpatterns()