from django.conf.urls import url
from . import appointments_views

urlpatterns = [
    url(r'^booking/', appointments_views.booking, name='booking'),
]
