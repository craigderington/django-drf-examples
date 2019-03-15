# -*- coding: utf-8 -*-
'''
Local settings
- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
'''

from .base import *

# DEBUG
DEBUG = True

# Allowed Hosts
ALLOWED_HOSTS = ['*']

# Mail Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.console'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[DRFExamples API] '
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''
SERVER_EMAIL = ''
SEND_BROKEN_LINK_EMAILS = True

# CACHING
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '/var/run/redis/redis.sock',
    },
}

# django-debug-toolbar
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}


# Test Runner
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


# Google Maps API Key
GOOGLE_API_KEY = ""
GOOGLE_MAPS_STATIC_KEY = ""
