from django.contrib import admin
from .models import Baggage, BoardingPass, Booking, FlightManifest, Passenger

# Register your models here.
admin.site.register(Baggage)
admin.site.register(BoardingPass)
admin.site.register(Booking)
admin.site.register(FlightManifest)
admin.site.register(Passenger)
