from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('map/', bfpmap, name='map'),
    path('incident_data/', incident_datasets, name="incidents"),
    path('barangay_incident_count/', barangay_incident_count, name='barangay_incident_count'),
    path('test/', test, name='test'),
    path('chart/', line_chart, name='line_chart'),
    path('chartJSON/', line_chart_json, name='line_chart_json'),
]
