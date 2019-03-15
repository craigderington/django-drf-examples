# coding: utf-8

from random import randint, randrange
from django.test import TestCase, RequestFactory
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
        request = self.factory.get('/locations')
        request.user = self.user
        # request.user = AnonymousUser()
        response = LocationList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def location_detail(self):
        request = self.factory.get('/locations/' + str(67367))
        request.user = self.user
        response = LocationDetail.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_geolocate(self):
        kwargs = {'ip_addr': str(self.ip)}
        request = self.factory.get('/geolocate/')
        request.user = self.user
        response = get_location(request, **kwargs)
        self.assertEqual(response.status_code, 201 or 200)
