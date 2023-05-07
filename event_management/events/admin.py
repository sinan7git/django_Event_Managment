from django.contrib import admin
from .models import Venue, EventUser, Event

# Register your models here.
admin.site.register(Venue)
admin.site.register(EventUser)
admin.site.register(Event)
