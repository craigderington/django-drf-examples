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
    dma_code = serializers.IntegerField()
    area_code = serializers.IntegerField()
    metro_code = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Location` instance, given the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Location` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)

        instance.save()
        return instance
