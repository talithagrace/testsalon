from django.shortcuts import render, get_object_or_404, redirect
from appointments.models import Availability, HairAppointment, Services
from django.utils import timezone
from .forms import SelectAvailabilityForm, CreateAppointmentForm, SelectServiceForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

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
            return render(request, 'appointments/booking.html', {'form': form})
    else:
        form = CreateAppointmentForm()
    return render(request, 'appointments/booking.html', {'form': form})
