from django.contrib import admin
from .models import City, Bus, Ticket

admin.site.register(City)
admin.site.register(Bus)
admin.site.register(Ticket)