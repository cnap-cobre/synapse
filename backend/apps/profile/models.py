from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from datetime import datetime, timedelta
from requests_oauthlib import OAuth2Session

from allauth.socialaccount.models import SocialAccount, SocialToken

from .util import get_refresh_token_url, get_protected_url

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100, default='', blank=True)
    
    def __str__(self):
        return str(self.user)

    @property
    def tokens(self):
        "Returns the tokens for a particular user"
        return SocialToken.objects.select_related('account').filter(account__user=self.user)

    def renew_tokens(self):
        now = timezone.now()
        expired_tokens = SocialToken.objects \
            .select_related('account').select_related('app') \
            .filter(account__user=self.user).filter(expires_at__lt=now)
        for tk in expired_tokens:
            token = {
                'access_token': tk.token,
                'refresh_token': tk.token_secret,
                'token_type': 'Bearer',
                'expires_in': (tk.expires_at - now).total_seconds()
            }
            client_id = tk.app.client_id
            refresh_url = get_refresh_token_url(tk.app)
            protected_url = get_protected_url(tk.app)

            extra = {
                'client_id': client_id,
                'client_secret': tk.app.secret
            }

            def token_saver(t):
                tk.token = t['access_token']
                tk.token_secret = t['refresh_token']
                tk.expires_at = datetime.fromtimestamp(int(t['expires_at']), tz=timezone.utc)
                tk.save()

            client = OAuth2Session(client_id, token=token, auto_refresh_url=refresh_url,
                auto_refresh_kwargs=extra, token_updater=token_saver)
            r = client.get(protected_url)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
