from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils import timezone
from django.template import RequestContext

def index(request):
    return render(request, 'home/index.html', {})

# Create your views here.
