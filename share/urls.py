from django.conf.urls.defaults import patterns, include, url

from share import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^albums/(\d+)/$', views.album, name='album'),
    url(r'^photos/(\d+)/$', views.photo, name='photo'),
)
