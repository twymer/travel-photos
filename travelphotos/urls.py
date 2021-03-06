from django.conf.urls import patterns, include, url
from django.conf import settings

from travelphotos import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^photos/', include('photos.urls', namespace='photos')),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),

    # Examples:
    # url(r'^$', 'travelphotos.views.home', name='home'),
    # url(r'^travelphotos/', include('travelphotos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
