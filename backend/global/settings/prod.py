from .base import *
from .secret import Secret

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1',
                 '172.18.0.1',
                 '127.18.0.3',
                 'localhost',
                 'synapse.ksu.edu',
                 '172.18.0.4']

CSRF_TRUSTED_ORIGINS += ['localhost']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'apprelay.smtp.ksu.edu'
DEFAULT_FROM_EMAIL = 'noreply@synapse.ksu.edu'

