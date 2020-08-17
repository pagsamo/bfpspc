from django.shortcuts import render
from django.core.serializers import serialize
from django.contrib.gis.serializers.geojson import Serializer
from django.http import HttpResponse
from .models import Incident, Barangay
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


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


def home(request):
    test = 'test'
    barangays = Barangay.objects.all()
    return render(request, 'index.html', {'test': test, 'barangays': barangays})


def bfpmap(request):
    return render(request, 'map.html')


def incident_datasets(request):
    incidents = serialize('geojson', Incident.objects.all())
    return HttpResponse(incidents, content_type="json")


def barangay_incident_count(request):
    geojsonformat = CustomSerializer().serialize(
        Barangay.objects.all(),
        geometry_field='Location',
        fields=(
            'Name',
            'IncidentCount'
        )
    )
    return HttpResponse(geojsonformat, content_type="json")


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='test.html')
line_chart_json = LineChartJSONView.as_view()

def test(request):
    return render(request, 'test.html')


def trythis():
    barangays = Barangay.objects.all()
    for b in barangays:
        if b.incident_set.all().count() != 0:
            print(b, b.incident_set.all().count())
