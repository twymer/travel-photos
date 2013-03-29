from django.conf.urls import patterns, include, url
from django.conf import settings

from photos import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<photo_id>\d+)/$', views.detail, name='detail'),
)
