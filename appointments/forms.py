from django import forms
from django.forms import widgets
from .models import Day, Availability, HairAppointment
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class SelectDaysForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ('day',)

class SelectAvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ('week_commencing', 'week_day', 'time',)
        widgets = {
            'week_commencing': DateInput()
        }

class CreateAppointmentForm(forms.ModelForm):
    class Meta:
        model = HairAppointment
        fields = ('phone_number', 'email', 'timeslot', 'style',)
