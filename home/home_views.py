from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.template import RequestContext
from appointments.models import Services

def index(request):
    services = Services.objects.all().order_by('price')
    return render(request, 'home/index.html', {'services': services})

def service_remove(request, pk):
    service = get_object_or_404(Services, pk=pk)
    service.delete()
    return redirect('home')
    # Create your views here.
