from rest_framework import serializers
from .models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    short_url = serializers.ReadOnlyField(source='bookmark.short_url')

    class Meta:
        model = Bookmark
        fields = ('id', 'name', 'full_url', 'short_url', 'created_date',
                  'modified_date', 'owner', 'favorite')
