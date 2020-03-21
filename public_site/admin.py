from django.contrib import admin
from .models import iqama, Prayer_time, events

admin.site.register(iqama)
admin.site.register(Prayer_time)
admin.site.register(events)