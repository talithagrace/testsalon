from django.shortcuts import render, get_object_or_404, redirect
from appointments.models import HairAppointment
from django.utils import timezone
from .forms import SelectAvailabilityForm, CreateAppointmentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def availability(request):
    if request.method == "POST":
        form = SelectAvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.user = request.user
            availability.save()
            return render(request, 'appointments/availability.html', {'form': form})
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
