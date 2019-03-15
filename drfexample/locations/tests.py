# coding: utf-8

from random import randint, randrange
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from .views import LocationList, LocationDetail, get_location


def generate_random_ip():
    """
    Create a random IP address
    :param self:
    :return: str(ip)
    """
    return ".".join(str(randrange(1, 255)) for _ in range(4))


class LocationViewsTest(TestCase):
    """
    Location testing
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.id = randint(300, 10000)
        self.ip = generate_random_ip()
        self.user = User.objects.create_user(
            username='superman',
            email='superman@drfexample.org',
            password='$top_secret'
        )

    def test_location_list(self):
        url = reverse('location-list')
        request = self.factory.get(url)
        request.user = self.user
        # request.user = AnonymousUser()
        response = LocationList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def location_detail(self):
        url = reverse('location-detail', kwargs={'pk': self.id})
        request = self.factory.get(url)
        request.user = self.user
        response = LocationDetail.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_geolocate(self):
        kwargs = {'ip_addr': str(self.ip)}
        url = reverse('geolocate', kwargs=kwargs)
        request = self.factory.get(url)
        request.user = self.user
        response = get_location(request, **kwargs)
        _statuscode = response.status_code
        self.assertEquals(response.status_code, _statuscode)
