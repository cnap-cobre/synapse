from django.utils import timezone

from apps.httpproxy.views import HttpProxy
from apps.profile.models import Profile

class AgaveProxy(HttpProxy):
    def get_auth_token(self, request):
        profile = Profile.from_user(request.user)
        agave_tokens = profile.tokens.filter(app__provider='agave')

        # 403 if the user has no token
        if not agave_tokens.exists():
            raise PermissionDenied('You must first authenticate against Agave.')

        assert agave_tokens.count() == 1
        token = agave_tokens.get()

        # Renew if token has expired
        if token.expires_at < timezone.now():
            print('Renewing tokens')
            profile.renew_tokens()
            return profile.tokens.filter(app__provider='agave').get().token

        return token.token
