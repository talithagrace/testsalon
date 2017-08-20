from django.conf.urls import url
from . import appointments_views

urlpatterns = [
    url(r'^booking/', appointments_views.booking, name='booking'),
    url(r'^availability/', appointments_views.availability, name='availability'),
    url(r'^services/', appointments_views.services, name='services'),
]
