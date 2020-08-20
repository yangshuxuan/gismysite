
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
class TrajectoryPlane(models.Model):

    # 轨迹ID
    trajectId = models.CharField(max_length=50,primary_key=True)

    # 轨迹时间序列
    timeSeries = ArrayField(models.DateTimeField())
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    trajectory=  models.LineStringField()


    # Returns the string representation of the model.
    def __str__(self):
        return self.trajectId