from django import forms
from django.forms import widgets
from .models import Day, Availability, HairAppointment, Services
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.utils.translation import ugettext_lazy as _


class DateInput(forms.DateInput):
    input_type = 'date'

class SelectServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ('styles', 'price',)

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

class CheckoutForm(forms.Form):
    payment_method_nonce = forms.CharField(
        max_length=1000,
        widget=forms.widgets.HiddenInput,
        required=False, # required field but this creates an exception message

    )
    def clean(self):
        self.cleaned_data = super(CheckoutForm, self).clean()
        #Braintree nonce is missing
        if not self.cleaned_data.get('payment_method_nonce'):
            raise forms.ValidationError(_(
            'We couldn\'t verify your payment. Please try again.'))
        return self.cleaned_data
