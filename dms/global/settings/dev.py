from .base import *

DEBUG=True
INSTALLED_APPS = ['debug_toolbar'] + INSTALLED_APPS
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INTERNAL_IPS = ['localhost', '127.0.0.1', '172.18.0.1', '172.18.0.3']
#ALLOWED_HOSTS += ['dms']


