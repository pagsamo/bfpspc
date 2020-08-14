from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Incident


def home(request):
    return render(request, 'test.html')

def map(request):
    return render(request, 'test.html')

def incident_datasets(request):
    incidents = serialize('geojson', Incident.objects.all())
    return HttpResponse(incidents, content_type="json")