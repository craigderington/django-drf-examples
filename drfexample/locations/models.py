from django.db import models

# Create your models here.


class Location(models.Model):
    """
    The Location data model for geo-coding
    """
    ip_addr = models.CharField(max_length=15, null=False, blank=False)
    time_zone = models.CharField(max_length=255, null=False, blank=False)
    latitude = models.FloatField(default=0.00)
    longitude = models.FloatField(default=0.00)
    region = models.CharField(max_length=255, null=False, blank=False)
    region_name = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    country_name = models.CharField(max_length=255, null=False, blank=False)
    country_code = models.CharField(max_length=255, null=False, blank=False)
    country_code3 = models.CharField(max_length=255, null=False, blank=False)
    postal_code = models.CharField(max_length=10, null=False, blank=False)
    dma_code = models.PositiveIntegerField(default=0)
    area_code = models.PositiveIntegerField(default=0)
    metro_code = models.PositiveIntegerField(default=0)

    def __str__(self):
        if self.region and self.city:
            return '{} from {} - {}'.format(
                self.ip_addr,
                self.region,
                self.postal_code
            )

    def get_latlng(self):
        if self.latitude and self.longitude:
            return 'Lat:{} Lng:{}'.format(
                self.latitude,
                self.longitude
            )
