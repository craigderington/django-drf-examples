from django.db import models
from string import ascii_lowercase, digits
from random import choices


class Bookmark(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    full_url = models.CharField(max_length=255, null=False, blank=False)
    short_url = models.CharField(max_length=50, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='bookmarks', on_delete=models.CASCADE)
    favorite = models.BooleanField(default=0)
    thumbnail_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.name:
            return '{}'.format(
                self.name
            )

    def save(self, *args, **kwargs):
        """
        Override the save method and create a short url
        """
        url = self.full_url.split('://')
        rand_str = ''.join(choices(ascii_lowercase + digits, k=10))
        self.short_url = url[0] + '://' + rand_str
        super(Bookmark, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
