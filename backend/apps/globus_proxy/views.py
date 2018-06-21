from django.utils import timezone
from django.conf import settings
from django.core.exceptions import PermissionDenied
from datetime import timedelta

from apps.httpproxy.views import HttpProxy
from apps.profile.models import Profile


class GlobusProxy(HttpProxy):
    base_url = settings.API_BASE_URL_GLOBUS
    rewrite = True

    def get_auth_token(self, request):
        profile = Profile.from_user(request.user)
        globus_tokens = profile.tokens.filter(app__provider='globus')

        # 403 if the user has no token
        if not globus_tokens.exists():
            raise PermissionDenied(
                    'You must first authenticate against Globus.'
            )

        assert globus_tokens.count() == 1
        token = globus_tokens.get()

        # Renew if token has expired
        if token.expires_at < timezone.now() + timedelta(hours=1):
            profile.renew_tokens()
            return profile.tokens.filter(app__provider='globus').get().token

        return token.token
