from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import GeoFeature


class GeoFeatureSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = GeoFeature
        geo_field = "geometry"
        fields = ['id', 'name', 'geometry']
