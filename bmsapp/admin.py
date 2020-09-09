from django.contrib import admin
from .models import Theatre,Movie,Seat,Tickets,City

# Register your models here.

admin.site.register(Theatre)
admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Tickets)
admin.site.register(City)
