from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name='homepage'),
    path('analytics/', analytics, name='analytics'),
    path('incident_datasets/', incident_datasets, name="incident_datasets"),
    path('barangay_incident_count/', barangay_incident_count, name='barangay_incident_count'),
    path('<int:incident_id>/apor_report/', apor_report, name='apor_report'),
    path('report_builder/',report_builder, name="report_builder"),
    path('new_incident/', new_incident, name="new_incident"),
    path('<int:incident_id>/apor/', apor, name='apor'),
    path('<int:incident_id>/apormulti/', apormulti, name='apormulti'),
    path('<int:incident_id>/update_incident/', update_incident, name='update_incident'),
    path('<int:incident_id>/spot/', spot, name='spot'),
    path('newstatusuponarrival/', newstatusuponarrival, name='newstatusuponarrival'),
    path('newresponsetime/', newresponsetime, name='newresponsetime'),
    path('newbreathing/', newbreathing, name='newbreathing'),
    path('newextinguish/', newextinguish, name='newextinguish'),
    path('newropeandladder/', newropeandladder, name='newropeandladder'),
    path('newhoseline/', newhoseline, name='newhoseline'),
    path('newdutypersonnel/', newdutypersonnel, name='newdutypersonnel'),
    path('newtimealarmstatus/', newtimealarmstatus, name='newtimealarmstatus'),
    path('deletestatusuponarrival/', deletestatusuponarrival, name='deletestatusuponarrival'),
    path('deleteresponsetime/', deleteresponsetime, name='deleteresponsetime'),
    path('deletebreathing/', deletebreathing, name='deletebreathing'),
    path('deleteextinguish/', deleteextinguish, name='deleteextinguish'),
    path('deleteropeandladder/', deleteropeandladder, name='deleteropeandladder'),
    path('deletehoseline/', deletehoseline, name='deletehoseline'),
    path('deletedutypersonnel/', deletedutypersonnel, name='deletedutypersonnel'),
    path('deletealarmstatus/', deletealarmstatus, name='deletealarmstatus'),
]
