from django import forms
from django.forms import widgets
from .models import Day, Availability, HairAppointment, Services
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views import generic

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

#class CheckoutView(generic.FormView):
#    """This view lets the user initiate a payment."""
#    form_class = forms.CheckoutForm
#    template_name = 'checkout.html'

#    @method_decorator(login_required)
#    def dispatch(self, request, *args, **kwargs):
        #we need the user to assign the transaction
#        self.user = request.user


        #switch to
#        if settings.BRAINTREE_PRODUCTION:
#            braintree_env = braintree.Environment.Production
#        else:
#            braintree_env = braintree.Environment.Sandbox

        #Configure braintree
#        braintree.Configuration.configure(
#            braintree_env,
#            merchant_id=settings.BRAINTREE_MERCHANT_ID,
#            public_key=settings.BRAINTREE_PUBLIC_KEY,
#            private_key=settings.BRAINTREE_PRIVATE_KEY,
#        )

        #generate a client token. This is sent to the form
        #to finally generate the payment nonce
        #can add something like {{"customer_id": 'foo'}}
