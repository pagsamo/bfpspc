from django import forms
from django.forms import ModelForm
from .models import AlarmStatusUponArrival, BreathingApparatus, Engines, ExtinguisingAgent, Incident, Barangay, IncidentResponse, Personnel, RopeAndLadder, HoseLine, TimeAlarmStatus
from leaflet.forms.widgets import LeafletWidget


class IncidentForm(ModelForm):
    DateAlarmReceived = forms.DateField(required=True, label="Date Alarm/Call Received")
    TimeAlarmReceived = forms.TimeField(required=True, label="Time Alarm/Call Received")
    Barangay = forms.ModelChoiceField(queryset=Barangay.objects.all())
    OwnerName = forms.CharField(max_length=200,required=True, label="Name of Owner")
    EstablishmentName = forms.CharField(max_length=200,required=True, label="Name of Establishment")
    HouseNumber = forms.CharField(max_length=50,required=True, label="House Number")
    Occupant = forms.CharField(max_length=200,required=True, label="Name of Occupant")
    

    class Meta:
        model = Incident
        fields = [
            'DateAlarmReceived',
            'TimeAlarmReceived',
            'Barangay',
            'HouseNumber',
            'Street',
            'OwnerName',
            'Occupant',
            'EstablishmentName',
            'Location',
            ]
        widgets = {
            'Location': LeafletWidget(),}


class APORMain(ModelForm):
    Caller = forms.CharField(max_length=200, label="Name of Caller", required=False)
    CallerAddress = forms.CharField(max_length=200, label="Address of Caller")
    PersonnelReceivingCall = forms.ModelChoiceField(queryset=Personnel.objects.all(), label="Personnel on Duty Receiving the Call", required=False)
    DateTimeUnderControl = forms.DateTimeField(label="Date Time Fire Under Control", required=False)
    DateTimeFireOut = forms.DateTimeField(label="Date/Time Fire Out", required=False)
    OCCUPANCYTYPE_CHOICES = [
        ('Structural/Residential', 'Structural/Residential'),
        ('Non Structural', 'Non Structural'),
        ('Vehicular','Vehicular'),
    ]
    OccupancyType = forms.ChoiceField(choices=OCCUPANCYTYPE_CHOICES, label="Type of Occupancy", required=False)
    OccupancyTypeRemarks = forms.CharField(max_length=200, label="Occupancy Type Remarks", required=False)
    class Meta:
        model = Incident
        fields = [
            'Caller',
            'CallerAddress',
            'PersonnelReceivingCall',
            'EstimatedDamageCost',
            'DateTimeUnderControl',
            'DateTimeFireOut',
            'OccupancyType',
            'OccupancyTypeRemarks',
            'DistanceFromBase',
            'DescriptionOfStructure',
            'InjuredCivilianM',
            'InjuredCivilianF',
            'InjuredFireFighterM',
            'InjuredFireFighterF',
            'DeathCivilianM',
            'DeathCivilianF',
            'DeathFireFighterM',
            'DeathFireFighterF',
            'Details',
            'Problems',
            'Observations',
            ]


class AlarmStatusUponArrivalForm(ModelForm):
    STATUS_CHOICES = [
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd','3rd'),
    ]
    StatusUponArrival = forms.ChoiceField(required=True,choices=STATUS_CHOICES,label="Status")
    StatusUponArrivalRemarks = forms.CharField(max_length=200,required=True, label="Remarks")
    class Meta:
        model = AlarmStatusUponArrival
        fields = [
            'StatusUponArrival',
            'StatusUponArrivalRemarks',
            ]
    

class IncidentResponseForm(ModelForm):
    Engine = forms.ModelChoiceField(required=True,queryset=Engines.objects.all())
    TimeDispatched = forms.TimeField(required=True,label="Time Dispatched")
    TimeArrived = forms.TimeField(required=True,label="Time Arrived")
    TimeReturnedToBase = forms.TimeField(required=True,label="Time Returned To Base")
    WaterTankRefilled = forms.IntegerField(required=True, label="Water Tank Refilled")
    GasConsumed = forms.IntegerField(required=True, label="Gas Consumed")
    class Meta:
        model = IncidentResponse
        fields = [
            'Engine',
            'TimeDispatched',
            'TimeArrived',
            'TimeReturnedToBase',
            'WaterTankRefilled',
            'GasConsumed',
            ]


class BreathingApparatusForm(ModelForm):
    BreathingApparatusNr = forms.IntegerField(required=True)
    BreathingApparatusType = forms.CharField(required=True, max_length=100)
    class Meta:
        model = BreathingApparatus
        fields = [
            'BreathingApparatusNr',
            'BreathingApparatusType',
        ]


class TimeAlarmStatusForm(ModelForm):
    STATUS_CHOICES = [
        ('1st Alarm', '1st Alarm'),
        ('2nd Alarm', '2nd Alarm'),
        ('3rd Alarm','3rd Alarm'),
        ('4th Alarm','4th Alarm'),
        ('5th Alarm','5th Alarm'),
        ('Task Force Alpha', 'Task Force Alpha'),
        ('Task Force Bravo', 'Task Force Bravo'),
        ('Task Force Charlie','Task Force Charlie'),
        ('Task Force Delta','Task Force Delta'),
        ('Task Force Echo','Task Foce Echo'),
        ('Task Force Hotel', 'Task Force Hotel'),
        ('Task Force India', 'Task Force India'),
        ('General Alarm', 'General Alarm'),
    ]
    AlarmStatus = forms.ChoiceField(required=True,choices=STATUS_CHOICES)
    AlarmTime = forms.TimeField(required=False)
    GroundCommander = forms.CharField(required=True, max_length=100)
    class Meta:
        model = TimeAlarmStatus
        fields = [
            'AlarmStatus',
            'AlarmTime',
            'GroundCommander',
        ]


class ExtinguisingAgentForm(ModelForm):
    Quantity = forms.IntegerField(required=True)
    Type = forms.CharField(required=True, max_length=100)
    class Meta:
        model = ExtinguisingAgent
        fields = [
            'Quantity',
            'Type',
        ]


class RopeAndLadderForm(ModelForm):
    Length = forms.IntegerField(required=True)
    Type = forms.CharField(required=True, max_length=100)
    class Meta:
        model = RopeAndLadder
        fields = [
            'Type',
            'Length',
        ]


class HoseLineForm(ModelForm):
    Nr = forms.IntegerField(required=True)
    Length = forms.IntegerField(required=True)
    Type = forms.CharField(required=True, max_length=100)
    class Meta:
        model = HoseLine
        fields = [
            'Nr',
            'Type',
            'Length'
        ]

class DutyPersonnelForm(ModelForm):
    Personnel = forms.ModelChoiceField(required=True, queryset=Personnel.objects.all())
    Designation = forms.CharField(required=True, max_length=100)
    Remarks = forms.CharField(required=True, max_length=100)
    class Meta:
        model = RopeAndLadder
        fields = [
            'Personnel',
            'Designation',
            'Remarks'
        ]


