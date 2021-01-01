from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import BreathingApparatus, ExtinguisingAgent, Rank, Personnel, Incident, Employee, AlarmStatusUponArrival, IncidentResponse, Engines
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User



class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)


@admin.register(ExtinguisingAgent)
class ExtinguisingAgentAdmin(LeafletGeoAdmin):
    list_display = ('Type', )


@admin.register(Engines)
class EnginesAdmin(LeafletGeoAdmin):
    list_display = ('Name', 'Model',)

@admin.register(BreathingApparatus)
class BreathingApparatusForm(LeafletGeoAdmin):
    list_display = ('BreathingApparatusType', )


@admin.register(IncidentResponse)
class IncidentResponseAdmin(LeafletGeoAdmin):
    list_display = ('Incident', 'Engine',)


@admin.register(AlarmStatusUponArrival)
class AlarmStatusUponArrivalAdmin(LeafletGeoAdmin):
    list_display = ('Incident', 'StatusUponArrival','StatusUponArrivalRemarks')

@admin.register(Rank)
class InvestigatorRankAdmin(LeafletGeoAdmin):
    list_display = ('Code', 'Definition',)
    
@admin.register(Personnel)
class InvestigatorAdmin(LeafletGeoAdmin):
    list_display = ('Rank', 'LastName', 'FirstName',)
    search_fields = ('Name',)

@admin.register(Incident)
class IncidentAdmin(LeafletGeoAdmin):
    list_display = ('DateAlarmReceived','OwnerName','Barangay',)
    # exclude = ('TotalFatalities','Approved',)
    search_fields = ('Barangay__Name', 'OwnerName',)
    filter = ('Barangay',)
    list_filter = ('Approved','Barangay',)
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     is_data = True if request.user.groups.all()[0].name == 'data-entry' else False
    #     disabled_fields = set()

    #     if is_data:
    #         disabled_fields |= {
    #             'Approved',
    #         }

    #     for f in disabled_fields:
    #         if f in form.base_fields:
    #             form.base_fields[f].disabled = True

    #     return form


admin.site.unregister(User)
admin.site.register(User, UserAdmin)