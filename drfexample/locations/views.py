from .models import Location
from .serializers import LocationSerializer
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import GeoIP
import ipaddress


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
@permission_classes((IsAuthenticated, ))
def get_location(request, *args, **kwargs):
    """
    Geolocate the given IP address from GeoCityLite and GeoIP
    :param request
    :param ip_addr:
    :return: geo_location
    """

    try:
        ip_addr = ipaddress.IPv4Address(kwargs['ip_addr'])

        try:
            gi_lookup = gi.record_by_addr(ip_addr.exploded)

            if gi_lookup:
                gi_lookup.update({'ip_addr': str(ip_addr.exploded)})
                serializer = LocationSerializer(data=gi_lookup)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(gi_lookup, status=status.HTTP_200_OK)

            else:
                data = {'ip_addr': str(ip_addr)}
                return Response(data, status=status.HTTP_200_OK)

        except IOError as err:
            data = {'Error': str(err)}
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except ipaddress.AddressValueError as ip_err:
        data = {'Error': str(ip_err)}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
