from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:

    url(r'^i18n/', include('django.conf.urls.i18n')),  # go to /i18n/setlang/
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('lander.urls', namespace='lander')),
    url(r'^members/', include('members.urls', namespace='members')),
    url(r'^photos/', include('photos.urls', namespace='photos')),
    url(r'^characters/', include('characters.urls', namespace='characters')),
)
