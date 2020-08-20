from django.contrib import admin

# Register your models here.
from Trajectory.models import TrajectoryPlane
from django.contrib.gis import admin

admin.site.register(TrajectoryPlane, admin.GeoModelAdmin)