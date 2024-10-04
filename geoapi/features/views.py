from rest_framework import viewsets
from rest_framework_gis.filters import InBBoxFilter
from .models import GeoFeature
from .serializers import GeoFeatureSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from rest_framework.permissions import AllowAny


class GeoFeatureViewSet(viewsets.ModelViewSet):
    queryset = GeoFeature.objects.all()
    serializer_class = GeoFeatureSerializer
    bbox_filter_field = 'geometry'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True

    # # Override global auth and permissions
    # permission_classes = [AllowAny]
    # authentication_classes = []
