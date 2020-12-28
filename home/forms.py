from django import forms
from django.forms import ModelForm
from .models import Incident, Barangay
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


class AporForm(ModelForm):
    Caller = forms.CharField(max_length=200,required=True, label="Name of Caller")
    CallerAddress = forms.CharField(max_length=200,required=True, label="Address of Caller")
    class Meta:
        model = Incident
        fields = [
            'Caller',
            'CallerAddress',
            ]

    
    