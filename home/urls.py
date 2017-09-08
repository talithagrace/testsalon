from django.conf.urls import url
from . import home_views

urlpatterns = [
    url(r'^$', home_views.index, name='home'),
    url(r'^service/(?P<pk>\d+)/remove/$', home_views.service_remove, name='service_remove'),
]
