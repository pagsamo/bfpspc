from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('map/', map, name='map'),
    path('incident_data/', incident_datasets, name="incidents"),
    path('barangay_incident_count/', barangay_incident_count, name='barangay_incident_count'),
    path('test/', test, name='test'),
]