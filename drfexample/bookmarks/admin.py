from django.contrib import admin
from .models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'full_url', 'created_date', 'favorite']
    search_fields = ['name', 'full_url']

    class Meta:
        ordering = ['-id']


admin.site.register(Bookmark, BookmarkAdmin)
