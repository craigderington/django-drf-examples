#!.env/bin/python
# coding: utf-8

from django.db import models
from datetime import datetime
import uuid


class ToDo(models.Model):
    """
    ToDo model class
    """
    TODO_STATUSES = (
        (0, 'Open'),
        (1, 'In Progress'),
        (2, 'Completed'),
        (3, 'Deferred'),
        (4, 'Closed No Resolution'),
        (5, 'Re-assigned'),
        (6, 'Transferred')
    )

    name = models.CharField(max_length=255, null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveIntegerField(null=False, choices=TODO_STATUSES, default=0)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey('auth.User', null=False, blank=False, on_delete=models.CASCADE)
    todo_uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        if self.name and self.status:
            return '{}'.format(
                self.name
            )

    def get_todo_status(self):
        return '{}'.format(
            self.status
        )

    def save(self, *args, **kwargs):
        if self.completed:
            self.completed_date = datetime.now()
        super(ToDo, self).save(*args, **kwargs)
