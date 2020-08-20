from django.contrib import admin

# Register your models here.
from world.models import WorldBorder
from django.contrib.gis import admin

admin.site.register(WorldBorder, admin.GeoModelAdmin)