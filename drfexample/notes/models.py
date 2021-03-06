from django.db import models
import uuid


class NoteTag(models.Model):
    """
    Note tags reference class
    """
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        if self.tag_name:
            return '{}'.format(self.tag_name)


class Note(models.Model):
    """
    Note model class
    """

    note_created_date = models.DateTimeField(auto_now_add=True)
    note_last_modified_date = models.DateTimeField()
    note_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    note_title = models.CharField(max_length=255, null=False, blank=False)
    note_text = models.TextField()
    note_image_src = models.URLField(null=True, blank=True, default=None)
    note_archived = models.BooleanField(default=False)
    note_pinned = models.BooleanField(default=False)
    note_color = models.CharField(max_length=20, default='#FFF')
    note_reminder = models.BooleanField(default=False)
    note_tags = models.ManyToManyField(NoteTag)
    owner = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)

    def __str__(self):
        if self.note_title and self.note_text:
            return '{}'.format(self.note_title)
        return '{}'.format(str(id))

    def save(self, *args, **kwargs):
        super(Note, self).save(*args, **kwargs)

    def get_image_url(self):
        if self.note_image_src:
            return '{}'.format(self.note_image_src)

    def get_tags(self):
        if self.note_tags:
            return '{}'.format(self.note_tags)


class NoteReminder(models.Model):
    """
    Note reminders class
    """

    REMINDER_TYPE_CHOICES = (
        ('Email', 'Email'),
        ('SMS', 'SMS'),
        ('Radio Waves', 'Radio Waves'),
        ('Laser Beam', 'Laser Beam'),
    )

    REMINDER_STATUSES = (
        (0, 'Created'),
        (1, 'Pending'),
        (2, 'Queued'),
        (4, 'Sent'),
        (5, 'Bounced'),
    )

    DELTA_TYPES = (
        ('seconds', 'seconds'),
        ('minutes', 'minutes'),
        ('hours', 'hours'),
        ('days', 'days'),
        ('weeks', 'weeks'),
        ('months', 'months'),
        ('years', 'years'),
        ('decades', 'decades'),
        ('centuries', 'centuries'),
    )

    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    reminder_type = models.CharField(max_length=50, default='Email', choices=REMINDER_TYPE_CHOICES)
    reminder_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    reminder_text = models.TextField()
    reminder_date = models.DateTimeField()
    reminder_notification_delta = models.PositiveIntegerField(default=30)
    reminder_notification_delta_type = models.CharField(max_length=50, default='minutes', choices=DELTA_TYPES)
    reminder_sent = models.BooleanField(default=False)
    reminder_sent_date = models.DateTimeField()
    reminder_status = models.PositiveIntegerField(choices=REMINDER_STATUSES)

    def __str__(self):
        if self.id and self.reminder_date:
            return '{} on {}'.format(
                self.reminder_type,
                self.reminder_date
            )

    def save(self, *args, **kwargs):
        super(NoteReminder, self).save(*args, **kwargs)

    def get_status(self):
        if self.reminder_status and self.reminder_sent_date:
            return '{} on {}'.format(
                self.reminder_status,
                self.reminder_sent_date
            )
        return '{}'.format(self.reminder_status)
