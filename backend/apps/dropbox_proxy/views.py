from django.conf import settings

from apps.httpproxy.views import HttpProxy
from apps.profile.models import Profile


class DropboxProxy(HttpProxy):
    base_url = settings.API_BASE_URL_DROPBOX

    def get_auth_token(self, request):
        profile = request.user.profile
        dropbox_tokens = profile.tokens.filter(app__provider='dropbox')

        # 403 if the user has no token
        if not dropbox_tokens.exists():
            raise PermissionDenied('You must first link your Dropbox account')

        return dropbox_tokens.get().token


class DropboxApiProxy(DropboxProxy):
    base_url = settings.API_BASE_URL_DROPBOX_API


class DropboxContentProxy(DropboxProxy):
    base_url = settings.API_BASE_URL_DROPBOX_CONTENT
