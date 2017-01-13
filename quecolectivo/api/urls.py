from django.conf.urls import url, include

from api import views

searchurl = r'^directions/(?P<lat_orig>[-+]?([0-9]*\.[0-9]+|[0-9]+)),(?P<lng_orig>[-+]?([0-9]*\.[0-9]+|[0-9]+))/(?P<lat_dest>[-+]?([0-9]*\.[0-9]+|[0-9]+)),(?P<lng_dest>[-+]?([0-9]*\.[0-9]+|[0-9]+))/(?P<rad>[0-9]+)/'

urlpatterns = [
    url(r'^search/(?P<lat_orig>[-+]?([0-9]*\.[0-9]+|[0-9]+)),(?P<lng_orig>[-+]?([0-9]*\.[0-9]+|[0-9]+))/(?P<lat_dest>[-+]?([0-9]*\.[0-9]+|[0-9]+)),(?P<lng_dest>[-+]?([0-9]*\.[0-9]+|[0-9]+))/(?P<rad>[0-9]+)/', views.search),
    url(r'route/(?P<pid>[0-9]+)/', views.routes),
    url(r'test/', views.test),
]