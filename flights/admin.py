from django.contrib import admin

#from .models import Airport, Flight
from .models import Airport, Flight, Passenger

# Register your models here.

#class FlightAdmin(admin.ModelAdmin):
#    list_display = ["id", "origin", "destination", "duration"]


class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ["flights"]

class AirportAdmin(admin.ModelAdmin):
    list_display = ['code', 'city']

class FlightAdmin(admin.ModelAdmin):
    list_display = ["id", "origin", "destination", "duration"]

admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
#admin.site.register(Flight)
admin.site.register(Passenger, PassengerAdmin)