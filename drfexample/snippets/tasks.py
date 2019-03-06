from __future__ import absolute_import
from datetime import datetime
from django.utils import timezone
from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Snippet

# task constants
timestamp = timezone.now()

# set up our logger utility
logger = get_task_logger(__name__)


def convert_datetime_object(o):
    if isinstance(o, datetime):
        return o.__str__()


@shared_task
def test_task(*args, **kwargs):
    return 'The test task executed with arguments: {} ' \
           'and keyword arguments: {}'.format(*args, **kwargs)


@shared_task
def get_snippet(snippet_pk_id):
    try:
        snippet = Snippet.objects.get(id=snippet_pk_id)
    except ObjectDoesNotExist as err:
        return '{}'.format(str(err))

    if snippet:
        return snippet
