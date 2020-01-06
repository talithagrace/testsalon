import braintree

from django.shortcuts import render, get_object_or_404, redirect
from appointments.models import Availability, HairAppointment, Services
from django.utils import timezone
from .forms import SelectAvailabilityForm, CreateAppointmentForm, SelectServiceForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from config import settings

from . import forms

#def availability(request):
#    if request.method == "POST":
#        form_1 = SelectAvailabilityForm(request.POST, prefix='available')
#        form_2 = SelectServiceForm(request.POST, prefix='services')

#        if form_1.is_valid() and form_2.is_valid():
#            availability = form_1.save(commit=False)
#            availability.user = request.user
#            availability.save()
#            services = form_2.save(commit=False)
#            services.user = request.user
#            services.save()
#            queryset_1 = Availability.objects.all().order_by('week_commencing', 'week_day')
#            quertset_2 = Services.objects.all()
#            context = {
#                'queryset1': queryset_1,
#                'queryset2': queryset_2,
#                'form1': form_1, #pass the form in the context
#                'form2': form_2
#            }
#            return render(request, 'appointments/availability.html', context)
#    else:
#        form_1 = SelectAvailabilityForm()
#        form_2 = SelectServiceForm
#    return render(request, 'appointments/availability.html', {'form1': form_1, 'form2': form_2})

def services(request):
    if request.method == "POST":
        form = SelectServiceForm(request.POST)
        if form.is_valid():
            services = form.save(commit=False)
            services.user = request.user
            services.save()
            queryset = Services.objects.all().order_by('price')
            context = {
                'queryset': queryset,
                'form': form
            }
            return render(request, 'appointments/services.html', context)
    else:
        form = SelectServiceForm()
    return render(request, 'appointments/services.html', {'form': form})


def availability(request):
    if request.method == "POST":
        form = SelectAvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.user = request.user
            availability.save()
            queryset = Availability.objects.all().order_by('week_commencing', 'week_day')
            context = {
                'queryset': queryset,
                'form': form #pass the form in the context
            }
            return render(request, 'appointments/availability.html', context)
    else:
        form = SelectAvailabilityForm()
    return render(request, 'appointments/availability.html', {'form': form})

def booking(request):
    if request.method == "POST":
        form = CreateAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            #return render(request, 'appointments/booking.html', {'form': form})
            return render(request, 'appointments/checkout.html', {'form': form})
            #redirect to checkout.html and add to urls aswell
    else:
        form = CreateAppointmentForm()
    #return render(request, 'appointments/booking.html', {'form': form})
    return render(request, 'appointments/booking.html', {'form': form})

class CheckoutView(generic.FormView):
    """This view lets the user initiate a payment."""
    form_class = forms.CheckoutForm
    template_name = 'appointments/checkout.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        #we need the user to assign the transaction
        self.user = request.user

        #this allows you to switch the braintree
        #environments by changing one setting

        if settings.BRAINTREE_PRODUCTION:
            braintree_env = braintree.Environment.Production
        else:
            braintree_env = braintree.Environment.Sandbox

        #configure braintree
        braintree.Configuration.configure(
            braintree_env,
            merchant_id=settings.BRAINTREE_MERCHANT_ID,
            public_key=settings.BRAINTREE_PUBLIC_KEY,
            private_key=settings.BRAINTREE_PRIVATE_KEY,
        )

        #generate a client token. this is sent to the form
        #to finally generate the payment nonce
        #youre able to add something like ''{"customer_id": 'foo'}'',
        #if youve already saved the ID
        self.braintree_client_token = braintree.ClientToken.generate({})
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(CheckoutView, self).get_context_data(**kwargs)
        ctx.update({
            'braintree_client_token': self.braintree_client_token,

        })
        return ctx

    def form_valid(self, form):
        #Braintree customer info, using the given data of the user instance
        customer_kwargs = {
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "email": self.user.email,
        }
        #create a new braintree customer
        result = braintree.Customer.create(customer_kwargs)
        if not result.is_success:
            context = self.get_context_data()
            #regenerate the form and display the relevant braintree Error
            context.update({
                'form': self.get_form(self.get_form_class()),
                'braintree_error': u'{} {}'.format(
                    result.message, _('Please get in contact.'))
            })
            return self.render_to_response(context)
        #if customer creation successful add customer id to user profile
        customer_id = result.customer.id

        #create a new transaction and submit it
        #best to use the whole address in production

        address_dict = {
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "street_address": 'street',
            "extended_address": 'street_2',
            "locality": 'city',
            "region": 'state_or_region',
            "postal_code": 'postal_code',
            "country_code_alpha2": 'alpha2_country_code',
            "country_code_alpha3": 'alpha3_country_code',
            "country_name": 'country',
            "country_code_numeric": 'numeric_country_code',
        }
        #use form to add a static amount
        result = braintree.Transaction.sale({
            "customer_id": customer_id,
            "amount": 10,
            "payment_method_nonce": form.cleaned_data['payment_method_nonce'],
            "descriptor": {
                #https://developers.braintreepayments.com/reference/general/validation-errors/all/python#descriptor
                "name": "COMPANY.*test",
            },
            "billing": address_dict,
            "shipping": address_dict,
            "options": {
                #use this option to store the customer data, if successful
                'store_in_vault_on_success': True,
                #use this option to directly settle the transaction

            }
        })
