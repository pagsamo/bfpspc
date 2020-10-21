from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Barangay, InvestigatorRank, Investigator, Incident, OccupancyType
from django.contrib.auth.models import User

# @admin.register(Barangay)
# class BarangayAdmin(LeafletGeoAdmin):
#     list_display = ('Name',)
#     search_fields = ('Name',)

@admin.register(InvestigatorRank)
class InvestigatorRankAdmin(LeafletGeoAdmin):
    list_display = ('Code', 'Definition',)
    
@admin.register(Investigator)
class InvestigatorAdmin(LeafletGeoAdmin):
    list_display = ('Rank', 'LastName', 'FirstName',)
    search_fields = ('Name',)

@admin.register(OccupancyType)
class OccupancyTypeAdmin(LeafletGeoAdmin):
    list_display = ('Description', )
    search_fields = ('Description',)

@admin.register(Incident)
class IncidentAdmin(LeafletGeoAdmin):
    list_display = ('OwnerEstablishmentName','DateTime','Barangay',)
    # exclude = ('TotalFatalities','Approved',)
    search_fields = ('Barangay__Name', 'OwnerEstablishmentName',)
    filter = ('Barangay',)
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_data = True if request.user.groups.all()[0].name == 'data-entry' else False
        disabled_fields = set()

        if is_data:
            disabled_fields |= {
                'Approved',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form