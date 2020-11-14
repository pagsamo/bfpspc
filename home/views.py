from django.shortcuts import render
from django.core.serializers import serialize
from django.contrib.gis.serializers.geojson import Serializer
from django.http import HttpResponse
from .models import Incident, Barangay


def week(i):
    switcher = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return switcher.get(i, "Invalid day of week")


def month(i):
    switcher = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec',
    }
    return switcher.get(i, "Invalid Month")


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
    barangays = Barangay.objects.all()
    incidents = Incident.objects.all().filter(Approved=True)
    earliest = incidents.earliest('DateTime')
    latest = incidents.latest('DateTime')
    perHour = {}
    for x in range(0, 24):
        perHour.update({x: incidents.filter(DateTime__hour=x).count()})
    perDay = {}
    for y in range(1, 8):
        perDay.update({week(y): incidents.filter(DateTime__week_day=y).count()})
    perYear = {}
    for z in range(earliest.DateTime.year, (latest.DateTime.year + 1)):
        perYear.update({z: incidents.filter(DateTime__year=z).count()})
    perMonth = {}
    for w in range(1, 13):
        perMonth.update({month(w): incidents.filter(DateTime__month=w).count()})
    overTime = {}
    for x in range(earliest.DateTime.year, (latest.DateTime.year + 1)):
        if x == earliest.DateTime.year:
            for y in range(earliest.DateTime.month, 13):
                overTime.update(
                    {"%s %s" % (month(y), x): incidents.filter(DateTime__year=x, DateTime__month=y).count()})
        elif x == latest.DateTime.year:
            for y in range(1, (latest.DateTime.month + 1)):
                overTime.update(
                    {"%s %s" % (month(y), x): incidents.filter(DateTime__year=x, DateTime__month=y).count()})
        else:
            for y in range(1, 13):
                overTime.update(
                    {"%s %s" % (month(y), x): incidents.filter(DateTime__year=x, DateTime__month=y).count()})
    return render(request, 'analytics.html',
                  {
                      'barangays': barangays,
                      'incidents': incidents,
                      'earliest': earliest,
                      'latest': latest,
                      'perHour': perHour,
                      'perDay': perDay,
                      'perYear': perYear,
                      'perMonth': perMonth,
                      'overTime': overTime
                  })


def incident_datasets(request):
    incidents = serialize('geojson', Incident.objects.all().filter(Approved=True))
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
