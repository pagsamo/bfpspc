from django import forms
from django.forms import ModelForm, widgets
from .models import Incident
from leaflet.forms.widgets import LeafletWidget
from bootstrap_datepicker_plus import DatePickerInput

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = [
            'DateAlarmReceived', 'TimeAlarmReceived', 'Barangay','Location', 'HouseNumber', 'Street','OwnerName','EstablishmentName'
            ]
        widgets = {
            'Location': LeafletWidget(),}
    