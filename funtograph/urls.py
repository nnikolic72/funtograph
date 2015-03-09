from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'funtograph.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')), # go to /i18n/setlang/
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('lander.urls', namespace='lander')),
)
