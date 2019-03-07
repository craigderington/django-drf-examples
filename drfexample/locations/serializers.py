from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    ip_addr = serializers.CharField(required=True, allow_blank=False, max_length=15)
    time_zone = serializers.CharField(required=True, allow_blank=False)
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)
    region = serializers.CharField(required=True, allow_blank=False, max_length=255)
    region_name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    city = serializers.CharField(required=True, allow_blank=False, max_length=255)
    country_name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    country_code = serializers.CharField(required=True, allow_blank=False, max_length=255)
    country_code3 = serializers.CharField(required=True, allow_blank=False, max_length=3)
    postal_code = serializers.CharField(required=True, allow_blank=False, max_length=10)
    dma_code = serializers.IntegerField(default=0)
    area_code = serializers.IntegerField(default=0)
    metro_code = serializers.IntegerField(default=0)

    def create(self, validated_data):
        """
        Create and return a new `Location` instance, given the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Location` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.ip_addr = validated_data.get('ip_addr', instance.ip_addr)
        instance.time_zone = validated_data.get('time_zone', instance.time_zone)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.region = validated_data.get('region', instance.region)
        instance.region_name = validated_data.get('region_name', instance.region_name)
        instance.city = validated_data.get('city', instance.city)
        instance.country_name = validated_data.get('country_name', instance.country_name)
        instance.country_code = validated_data.get('country_code', instance.country_code)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.dma_code = validated_data.get('dma_code', instance.dma_code)
        instance.area_code = validated_data.get('area_code', instance.area_code)
        instance.metro_code = validated_data.get('metro_code', instance.metro_code)
        instance.save()
        return instance
