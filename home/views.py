from django.shortcuts import render
from django.core.serializers import serialize
from django.contrib.gis.serializers.geojson import Serializer
from django.http import HttpResponse
from .models import Incident, Barangay



class CustomSerializer(Serializer):

    def end_object(self, obj):
        for field in self.selected_fields:
            if field == self.geometry_field or field == 'pk':
                continue
            elif field in self._current.keys():
                continue
            else:
                try:
                    self._current[field] = getattr(obj, field)()
                except AttributeError:
                    pass
        super(CustomSerializer, self).end_object(obj)


def homepage(request):
    return render(request, 'map.html')


def analytics(request):
    test = 'test'
    barangays = Barangay.objects.all()
    return render(request, 'index.html', {'test': test, 'barangays': barangays})


def incident_datasets(request):
    incidents = serialize('geojson', Incident.objects.all())
    return HttpResponse(incidents, content_type="json")


def barangay_incident_count(request):
    geojsonformat = CustomSerializer().serialize(
        Barangay.objects.all(),
        geometry_field='geom',
        fields=(
            'Name',
            'IncidentCount'
        )
    )
    return HttpResponse(geojsonformat, content_type="json")

