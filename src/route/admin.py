from django.contrib import admin
from .models import *


class PlanesAdmin(admin.ModelAdmin):
    list_display = ['plain_code', 'plain_start', 'plain_end', 'trip_time']


admin.site.register(Cities)
admin.site.register(Planes, PlanesAdmin)
