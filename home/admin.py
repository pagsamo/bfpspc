from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Barangay, Rank, Personnel, Incident
from django.contrib.auth.models import User



# @admin.register(Barangay)
# class BarangayAdmin(LeafletGeoAdmin):
#     list_display = ('Name',)
#     search_fields = ('Name',)

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