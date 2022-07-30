from django.contrib import admin
from .models import Vessel

# Register your models here.


class VesselAdmin(admin.ModelAdmin):
    list_display = ('datetime','name', 'callsign', 'latitude', 'longitude', 
                    'destination', 'eta', 'course','speed','mmsi', 'heading', 'navstat', 'imo', 'aistype','a','b','c','draught')

    

admin.site.register(Vessel, VesselAdmin)