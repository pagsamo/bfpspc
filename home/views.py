from django.core import paginator
from django.http.response import Http404, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize
from django.contrib.gis.serializers.geojson import Serializer
from django.http import HttpResponse, HttpResponseRedirect
from .models import AlarmStatusUponArrival, BreathingApparatus, DutyPersonnel, ExtinguisingAgent, HoseLine, Incident, Barangay, Engines, IncidentResponse, Personnel, RopeAndLadder, TimeAlarmStatus
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator
from .forms import BreathingApparatusForm, DutyPersonnelForm, ExtinguisingAgentForm, HoseLineForm, IncidentForm, APORMain, AlarmStatusUponArrivalForm, IncidentResponseForm, RopeAndLadderForm, TimeAlarmStatusForm

@login_required(login_url='/accounts/login')
def report(request, incident_id):
    incident = Incident.objects.get(id=incident_id)
    return render(request, 'report.html',{
        "incident": incident,
    })


@login_required(login_url='/accounts/login')
def apor(request, incident_id):
    incident = get_object_or_404(Incident, id=incident_id)
    if request.method == "POST":
        form = APORMain(request.POST, instance=incident)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponseRedirect('/'+str(incident_id)+'/apormulti/')
    else:
        aporMain = APORMain(request.POST or None, instance=incident)
    return render(request,'apor.html', {
        "aporMain": aporMain,
        "incident": incident,
    })

    
################################
#newstatusuponarrival
################################
def newstatusuponarrival(request):
    if request.is_ajax():
        response_data = {}
        id = request.POST.get('Incident_id')
        i = Incident.objects.get(id=id)
        StatusUponArrival = request.POST.get('status')
        StatusUponArrivalRemarks = request.POST.get('remarks')

        response_data['Incident_id'] = id
        response_data['StatusUponArrival'] = StatusUponArrival
        response_data['StatusUponArrivalRemarks'] = StatusUponArrivalRemarks

        newalarm = AlarmStatusUponArrival.objects.create(
            Incident = i,
            StatusUponArrival = StatusUponArrival,
            StatusUponArrivalRemarks = StatusUponArrivalRemarks,
        )
        response_data['new_id'] = newalarm.id
        return JsonResponse(response_data)

################################
#newresponsetime
################################


def newresponsetime(request):
    if request.is_ajax():
        response_data = {}
        id = request.POST.get('Incident_id')
        i = Incident.objects.get(id=id)
        engine_id = request.POST.get('engine')
        Engine = Engines.objects.get(id=engine_id)
        TimeDispatched = request.POST.get('timedispatched')
        TimeArrived = request.POST.get('timearrived')
        TimeReturnedToBase = request.POST.get('timereturnedtobase')
        WaterTankRefilled = request.POST.get('watertankrefilled')
        GasConsumed = request.POST.get('gasconsumed')

        response_data['Incident_id'] = id
        response_data['Engine'] = Engine.Name
        response_data['TimeDispatched'] = TimeDispatched
        response_data['TimeArrived'] = TimeArrived
        response_data['TimeReturnedToBase'] = TimeReturnedToBase
        response_data['WaterTankRefilled'] = WaterTankRefilled
        response_data['GasConsumed'] = GasConsumed

        newresponsetime = IncidentResponse.objects.create(
            Incident = i,
            Engine = Engine,
            TimeDispatched = TimeDispatched,
            TimeArrived = TimeArrived,
            TimeReturnedToBase = TimeReturnedToBase,
            WaterTankRefilled = WaterTankRefilled,
            GasConsumed = GasConsumed,
        )
        response_data['new_id'] = newresponsetime.id
        newresponsetime = IncidentResponse.objects.get(id=newresponsetime.id)
        response_data['responsetime'] = newresponsetime.ResponseTime()
        return JsonResponse(response_data)
################################
#newresponsetime
################################


################################
#newbreathing
################################
def newbreathing(request):
    if request.is_ajax():
        response_data = {}
        id = request.POST.get('Incident_id')
        i = Incident.objects.get(id=id)
        BreathingApparatusNr = request.POST.get('nr')
        BreathingApparatusType = request.POST.get('type')

        response_data['Incident_id'] = id
        response_data['BreathingApparatusNr'] = BreathingApparatusNr
        response_data['BreathingApparatusType'] = BreathingApparatusType

        newbreathing = BreathingApparatus.objects.create(
            Incident = i,
            BreathingApparatusNr = BreathingApparatusNr,
            BreathingApparatusType = BreathingApparatusType,
        )
        response_data['new_id'] = newbreathing.id
        return JsonResponse(response_data)

################################
#newbreathing
################################


################################
#newbreathing
################################
def newextinguish(request):
    if request.is_ajax():
        response_data = {}
        id = request.POST.get('Incident_id')
        i = Incident.objects.get(id=id)
        Quantity = request.POST.get('qty')
        Type = request.POST.get('type')

        response_data['Incident_id'] = id
        response_data['Quantity'] = Quantity
        response_data['Type'] = Type

        newex = ExtinguisingAgent.objects.create(
            Incident = i,
            Quantity = Quantity,
            Type = Type,
        )
        response_data['new_id'] = newex.id
        return JsonResponse(response_data)

################################
#newbreathing
################################


################################
#newropeandladder
################################
def newropeandladder(request):
    if request.is_ajax():
        response_data = {}
        id = request.POST.get('Incident_id')
        i = Incident.objects.get(id=id)
        Length = request.POST.get('length')
        Type = request.POST.get('type')

        response_data['Incident_id'] = id
        response_data['Length'] = Length
        response_data['Type'] = Type

        newrl = RopeAndLadder.objects.create(
            Incident = i,
            Length = Length,
            Type = Type,
        )
        response_data['new_id'] = newrl.id
        return JsonResponse(response_data)

################################
#newropeandladder
################################


################################
#newhoseline
################################
def newhoseline(request):
    if request.is_ajax():
        response_data = {}
        id = request.POST.get('Incident_id')
        i = Incident.objects.get(id=id)
        Length = request.POST.get('length')
        Type = request.POST.get('type')
        Nr = request.POST.get('nr')

        response_data['Incident_id'] = id
        response_data['Nr'] = Nr
        response_data['Length'] = Length
        response_data['Type'] = Type

        newhl = HoseLine.objects.create(
            Incident = i,
            Nr = Nr,
            Type = Type,
            Length = Length,
        )
        response_data['new_id'] = newhl.id
        return JsonResponse(response_data)

################################
#newhoseline
################################

################################
#newdutypersonnel
################################
def newdutypersonnel(request):
    if request.is_ajax():
        response_data = {}
        id = request.POST.get('Incident_id')
        i = Incident.objects.get(id=id)
        personnel_id = request.POST.get('personnel_id')
        p = Personnel.objects.get(id=personnel_id)
        Designation = request.POST.get('designation')
        Remarks = request.POST.get('remarks')

        response_data['Incident_id'] = id
        response_data['personnel_id'] = personnel_id
        response_data['Personnel'] = p.full()
        response_data['Designation'] = Designation
        response_data['Remarks'] = Remarks

        newd = DutyPersonnel.objects.create(
            Incident = i,
            Personnel = p,
            Designation = Designation,
            Remarks = Remarks,
        )
        response_data['new_id'] = newd.id
        return JsonResponse(response_data)

################################
#newdutypersonnel
################################


################################
#deletedutypersonnel
################################
def deletedutypersonnel(request):
    if request.is_ajax():
        sa_id = request.POST.get('sa_id')
        response_data = {}
        response_data['sa_id'] = sa_id
        duty = DutyPersonnel.objects.get(id=sa_id)
        duty.delete()
        return JsonResponse(response_data)
################################
#deletedutypersonnel
################################


################################
#newtimealarmstatus
################################
def newtimealarmstatus(request):
    if request.is_ajax():
        response_data = {}
        id = request.POST.get('Incident_id')
        i = Incident.objects.get(id=id)
        AlarmStatus = request.POST.get('alarmstatus')
        AlarmTime = request.POST.get('alarmtime')
        GroundCommander = request.POST.get('groundcommander')

        response_data['Incident_id'] = id
        response_data['AlarmStatus'] = AlarmStatus
        response_data['AlarmTime'] = AlarmTime
        response_data['GroundCommander'] = GroundCommander

        newta = TimeAlarmStatus.objects.create(
            Incident = i,
            AlarmStatus = AlarmStatus,
            AlarmTime = AlarmTime,
            GroundCommander = GroundCommander,
        )
        response_data['new_id'] = newta.id
        return JsonResponse(response_data)

################################
#newtimealarmstatus
################################


################################
#deletealarmstatus
################################
def deletealarmstatus(request):
    if request.is_ajax():
        sa_id = request.POST.get('sa_id')
        response_data = {}
        response_data['sa_id'] = sa_id
        duty = TimeAlarmStatus.objects.get(id=sa_id)
        duty.delete()
        return JsonResponse(response_data)
################################
#deletealarmstatus
################################


################################
#deletestatusuponarrival
################################
def deletestatusuponarrival(request):
    if request.is_ajax():
        sa_id = request.POST.get('sa_id')
        response_data = {}
        response_data['sa_id'] = sa_id
        statusuponarrival = AlarmStatusUponArrival.objects.get(id=sa_id)
        statusuponarrival.delete()
        return JsonResponse(response_data)
################################
#deletestatusuponarrival
################################

################################
#deletebreathing
################################
def deletebreathing(request):
    if request.is_ajax():
        sa_id = request.POST.get('sa_id')
        response_data = {}
        response_data['sa_id'] = sa_id
        breathing = BreathingApparatus.objects.get(id=sa_id)
        breathing.delete()
        return JsonResponse(response_data)
################################
#deletestatusuponarrival
################################


################################
#deletebreathing
################################
def deleteextinguish(request):
    if request.is_ajax():
        sa_id = request.POST.get('sa_id')
        response_data = {}
        response_data['sa_id'] = sa_id
        extin = ExtinguisingAgent.objects.get(id=sa_id)
        extin.delete()
        return JsonResponse(response_data)
################################
#deletestatusuponarrival
################################


################################
#deletebreathing
################################
def deleteropeandladder(request):
    if request.is_ajax():
        sa_id = request.POST.get('sa_id')
        response_data = {}
        response_data['sa_id'] = sa_id
        extin = RopeAndLadder.objects.get(id=sa_id)
        extin.delete()
        return JsonResponse(response_data)
################################
#deletestatusuponarrival
################################



################################
#delethoseline
################################
def deletehoseline(request):
    if request.is_ajax():
        sa_id = request.POST.get('sa_id')
        response_data = {}
        response_data['sa_id'] = sa_id
        extin = HoseLine.objects.get(id=sa_id)
        extin.delete()
        return JsonResponse(response_data)
################################
#delethoseline
################################

################################
#deleteresponsetime
################################
def deleteresponsetime(request):
    if request.is_ajax():
        sa_id = request.POST.get('sa_id')
        response_data = {}
        response_data['sa_id'] = sa_id
        incidentresponse = IncidentResponse.objects.get(id=sa_id)
        incidentresponse.delete()
        return JsonResponse(response_data)
################################
#deleteresponsetime
################################ 


@login_required(login_url='/accounts/login')
def apormulti(request, incident_id):
    incident = get_object_or_404(Incident, id=incident_id)
    f_alarmstatusuponarrival = AlarmStatusUponArrivalForm()
    f_responsetime = IncidentResponseForm()
    f_breathing = BreathingApparatusForm()
    f_extinguish = ExtinguisingAgentForm()
    f_rl = RopeAndLadderForm()
    f_hl = HoseLineForm()
    f_duty = DutyPersonnelForm()
    f_ta = TimeAlarmStatusForm()
    return render(request, 'apormulti.html',{
        "incident": incident,
        "f_alarmstatusuponarrival": f_alarmstatusuponarrival,
        "f_responsetime": f_responsetime,
        "f_breathing": f_breathing,
        "f_extinguish": f_extinguish,
        "f_rl": f_rl,
        "f_hl": f_hl,
        "f_duty": f_duty,
        "f_ta": f_ta,
    })


@login_required(login_url='/accounts/login')
def new_incident(request):
    if request.method == "POST":
        form = IncidentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponseRedirect("/"+str(form.id)+'/apor/')
    else:
        form = IncidentForm()
    return render(request, 'new_incident.html',{'form':form})

@login_required(login_url='/accounts/login')
def update_incident(request, incident_id):
    incident = Incident.objects.get(id=incident_id)
    if request.method == "POST":
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponseRedirect("/"+str(incident_id)+'/apor/')
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'incident.html',{
        'form':form,
        'incident': incident,
        })


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