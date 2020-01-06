from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import RequestContext
from appointments.models import Services, HairAppointment
from appointments.forms import CreateAppointmentForm


def index(request):
    services = Services.objects.all().order_by('price')
    if request.method == "POST":
        form = CreateAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            context = {
                'form': form,
                'services': services
            }
            #return render(request, 'appointments/booking.html', {'form': form})
            return render(request, 'home/newsalonbase.html', context)
    else:
        form = CreateAppointmentForm()
        context = {
            'form': form,
            'services': services
        }
    #return render(request, 'appointments/booking.html', {'form': form})
    return render(request, 'home/newsalonbase.html', context)


def service_remove(request, pk):
    service = get_object_or_404(Services, pk=pk)
    service.delete()
    return redirect('home')
    # Create your views here.
