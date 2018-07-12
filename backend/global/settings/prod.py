from .base import *
from .secret import Secret

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1',
                 '172.18.0.1',
                 '127.18.0.3',
                 'localhost',
                 'dataverse.cnap.ksu.edu',
                 '172.18.0.4']

CSRF_TRUSTED_ORIGINS += ['localhost']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'