from .models import Location
from .serializers import LocationSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions
import GeoIP
from rest_framework.decorators import api_view

gi = GeoIP.open('/var/lib/geoip/GeoLiteCity.dat', GeoIP.GEOIP_INDEX_CACHE | GeoIP.GEOIP_CHECK_CACHE)


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


@api_view(['GET'])
def get_location(request, *args, **kwargs):
    """
    Geolocate the given IP address from GeoCityLite and GeoIP
    :param request
    :param ip_addr:
    :return: geo_location
    """
    ip_addr = kwargs['ip_addr']
    gi_lookup = gi.record_by_addr(ip_addr)
    return Response(gi_lookup)
