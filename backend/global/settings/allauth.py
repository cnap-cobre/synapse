ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_USERNAME_BLACKLIST = ['admin']

# Confirmation Email
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Synapse Email Confirmation"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/"

SOCIALACCOUNT_PROVIDERS = {
    'globus': {
        'SCOPE': [
            'openid',
            'profile',
            'offline_access',
            'email',
            'urn:globus:auth:scope:transfer.api.globus.org:all'
        ]
    },
    'agave': {
        'API_URL': 'https://api.tacc.utexas.edu'
    },
    'jupyterhub': {
        'API_URL': 'https://jupyterhub.beocat.ksu.edu'
    }
}
