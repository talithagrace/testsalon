from django.contrib import admin
from .models import Day, Availability, HairAppointment, Services

admin.site.register(Day)
admin.site.register(Availability)
admin.site.register(HairAppointment)
admin.site.register(Services)

# Register your models here.
