from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    url(r'^', include('lander.urls', namespace='lander')),
    url(r'^i18n/', include('django.conf.urls.i18n')),  # go to /i18n/setlang/
    url(r'^admin/', include(admin.site.urls)),

)
