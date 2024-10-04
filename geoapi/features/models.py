from django.contrib.gis.db import models


class GeoFeature(models.Model):
    name = models.CharField(max_length=255)
    geometry = models.GeometryField()

    def __str__(self):
        return self.name
