from django import forms
from django.forms import ModelForm, widgets
from .models import Incident
from leaflet.forms.widgets import LeafletWidget

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = ['DateCalled', 'Barangay','Location', 'HouseNumber', 'Street','OwnerName','EstablishmentName']
        widgets = {
            'Location': LeafletWidget(), }
    