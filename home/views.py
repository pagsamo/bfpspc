from django.core import paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.core.serializers import serialize
from django.contrib.gis.serializers.geojson import Serializer
from django.http import HttpResponse, HttpResponseRedirect
from .models import Incident, Barangay
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator
from .forms import IncidentForm, AporForm

def apor(request, incident_id):
    incident = get_object_or_404(Incident, id=incident_id)
    form = AporForm()
    if request.method == "POST":
        form = AporForm(request.POST, instance=incident)
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect('/')
    return render(request,'apor.html', {
        "form": form,
        "incident": incident,
    })


def new_incident(request):
    form = IncidentForm()
    if request.method == "POST":
        form = IncidentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponseRedirect(str(form.id)+'/apor/')
    else:
        form = IncidentForm()
    return render(request, 'new_incident.html',{'form':form})


@login_required(login_url='/accounts/login')
def report(request):
    if request.method == "POST":
        # csrfmiddlewaretokendateFromdateTo
        checked = []
        for ck in request.POST:
            if ck != "csrfmiddlewaretoken" and ck != "dateFrom" and ck !=  "dateTo" and ck != "barangay":
                checked.append(ck)

        dateFrom = request.POST.get("dateFrom")
        dateTo = request.POST.get("dateTo")
        incidents = Incident.objects.filter(DateAlarmReceived__range=[dateFrom, dateTo])
        incident_parse = []
        for i in incidents:
            incl = {}
            for c in checked:
                incl[c] = getattr(i, c)
            incident_parse.append(incl)

        # return HttpResponse(checked_test)

        return render(request, 'reports.html', {
            "incidents": incident_parse,
            "checked": checked,
        })


@login_required(login_url='/accounts/login')
def report_builder(request):
    incidents = Incident.objects.all()
    barangay = Barangay.objects.all()
    if request.GET.get('order'):
        ord = request.GET.get('order')
        if(ord=="date-asc"):
            incidents = incidents.order_by('DateAlarmReceived')
        elif(ord=="date-desc"):
            incidents = incidents.order_by('-DateAlarmReceived')
        elif(ord=="barangay-asc"):
            incidents = incidents.order_by('Barangay')
        elif(ord=="barangay-desc"):
            incidents = incidents.order_by('-Barangay')
        elif(ord=='owner-asc'):
            incidents = incidents.order_by('OwnerName')
        elif(ord=='owner-desc'):
            incidents = incidents.order_by('-OwnerName')
    if(request.GET.get('barangay') and request.GET.get('dateFrom') and request.GET.get('dateTo')):
        q_brgy = request.GET.get('barangay')
        incidents = incidents.filter(Barangay=q_brgy)
        dateFrom = request.GET.get('dateFrom')
        dateTo = request.GET.get('dateTo')
        incidents = incidents.filter(DateAlarmReceived__range=[dateFrom, dateTo])

    if request.GET.get('barangay'):
        q_brgy = request.GET.get('barangay')
        incidents = incidents.filter(Barangay=q_brgy)

    if (request.GET.get('dateFrom') and request.GET.get('dateTo')):
        dateFrom = request.GET.get('dateFrom')
        dateTo = request.GET.get('dateTo')
        incidents = incidents.filter(DateAlarmReceived__range=[dateFrom, dateTo])

    paginator = Paginator(incidents, 20)
    page = request.GET.get('page')
    try:
        incidents = paginator.page(page)
    except PageNotAnInteger:
        incidents = paginator.page(1)
    return render(request, 'report_builder.html',{"incidents": incidents,'page':page,"barangay":barangay,})


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


@login_required(login_url='/accounts/login')
def homepage(request):
    return render(request, 'map.html')


@login_required(login_url='/accounts/login')
def analytics(request):
    prompt = ''
    barangays = Barangay.objects.all()
    if request.method == "POST":
        dateFrom = request.POST.get('dateFrom')
        dateTo = request.POST.get('dateTo')
        incidents = Incident.objects.filter(DateAlarmReceived__range=[dateFrom, dateTo])
        if not incidents:
            prompt = dateFrom + " to " + dateTo + " returned no results"
            incidents = Incident.objects.all().filter(Approved=True)
            earliest = incidents.earliest('DateAlarmReceived')
            latest = incidents.latest('DateAlarmReceived')
            perBarangay = {}
            for b in barangays:
                perBarangay.update({b.Name: b.incident_set.filter(DateAlarmReceived__range=[earliest.DateAlarmReceived, latest.DateAlarmReceived]).count()})
        else:
            earliest = incidents.earliest('DateAlarmReceived')
            latest = incidents.latest('DateAlarmReceived')
            perBarangay = {}
            for b in barangays:
                perBarangay.update({b.Name: b.incident_set.filter(DateAlarmReceived__range=[dateFrom, dateTo]).count()})
    else:
        incidents = Incident.objects.all().filter(Approved=True)
        earliest = incidents.earliest('DateAlarmReceived')
        latest = incidents.latest('DateAlarmReceived')
        perBarangay = {}
        for b in barangays:
            perBarangay.update({b.Name: b.incident_set.filter(DateAlarmReceived__range=[earliest.DateAlarmReceived, latest.DateAlarmReceived]).count()})


    perHour = {}
    for x in range(0, 24):
        perHour.update({x: incidents.filter(TimeAlarmReceived__hour=x).count()})
    perDay = {}
    for y in range(1, 8):
        perDay.update({week(y): incidents.filter(DateAlarmReceived__week_day=y).count()})
    perYear = {}
    for z in range(earliest.DateAlarmReceived.year, (latest.DateAlarmReceived.year + 1)):
        perYear.update({z: incidents.filter(DateAlarmReceived__year=z).count()})
    perMonth = {}
    for w in range(1, 13):
        perMonth.update({month(w): incidents.filter(DateAlarmReceived__month=w).count()})
    overTime = {}
    for x in range(earliest.DateAlarmReceived.year, (latest.DateAlarmReceived.year + 1)):
        if x == earliest.DateAlarmReceived.year:
            for y in range(earliest.DateAlarmReceived.month, 13):
                overTime.update(
                    {"%s %s" % (month(y), x): incidents.filter(DateAlarmReceived__year=x, DateAlarmReceived__month=y).count()})
        elif x == latest.DateAlarmReceived.year:
            for y in range(1, (latest.DateAlarmReceived.month + 1)):
                overTime.update(
                    {"%s %s" % (month(y), x): incidents.filter(DateAlarmReceived__year=x, DateAlarmReceived__month=y).count()})
        else:
            for y in range(1, 13):
                overTime.update(
                    {"%s %s" % (month(y), x): incidents.filter(DateAlarmReceived__year=x, DateAlarmReceived__month=y).count()})
    return render(request, 'analytics.html',
                  {
                      'barangays': barangays,
                      'incidents': incidents,
                      'perHour': perHour,
                      'perDay': perDay,
                      'perYear': perYear,
                      'perMonth': perMonth,
                      'overTime': overTime,
                      'perBarangay': perBarangay,
                      'prompt': prompt,
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

@login_required(login_url='/accounts/login')
def reports(request):
    return render(request, 'reports.html')


def error_404(request, exception):
    return render(request, '404.html')