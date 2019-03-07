from django.contrib import admin
from .models import Location
# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    list_display = ['ip_addr', 'region_name', 'country_name', 'time_zone', 'latitude', 'longitude']
    search_fields = ['ip_addr', 'region_name', 'latitude', 'longitude']
    list_filter = ['region_name', 'time_zone']

    class Meta:
        ordering = ['region']


admin.site.register(Location, LocationAdmin)
