from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Barangay, InvestigatorRank, Investigator, Incident, OccupancyType

@admin.register(Barangay)
class BarangayAdmin(LeafletGeoAdmin):
    list_display = ('Name',)
    search_fields = ('Name',)

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
    list_display = ('DateTime', 'Barangay', 'OwnerEstablishmentName',)
    exclude = ('TotalFatalities',)
    search_fields = ('DateTime', 'Barangay', 'OwnerEstablishment',)
    filter = ('Barangay',)
