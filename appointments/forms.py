#from django import forms
#from django.forms import widgets
#from .models import HairAppointment
#from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

#class DateInput(forms.DateInput):
    input_type = 'date'

#class CreateAppointmentForm(forms.ModelForm):
#    class Meta:
#        model = HairAppointment
#        fields = ('phone_number', 'email', 'date', 'timeslot', 'style' )
#        widgets = {
#            'date': DateInput()
#        }
