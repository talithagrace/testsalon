from django.conf.urls import url
from . import home_views

urlpatterns = [
    url(r'^$', home_views.index, name='home'),
]
