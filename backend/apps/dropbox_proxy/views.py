import requests
from django.conf import settings
from django.http import HttpResponse
import json
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

    def get(self, request, *args, **kwargs):
        headers = {
            'Authorization': 'Bearer ' + self.get_auth_token(request),
        }
        request_url = self.get_full_url(self.url)
        if '/2/files/download' in request_url:
            filepath = request_url[len(self.base_url + '/2/files/download'):]
            headers['Dropbox-API-Arg'] = json.dumps({'path': filepath})
            response = requests.post(request_url[0:len(self.base_url +
                '/2/files/download')], headers=headers)
            print("filepath", filepath, "headers", headers, "response", response)
        else:
            response = requests.get(request_url, headers=headers)
        django_response = HttpResponse(response, status=response.status_code)
        for header in response.headers:
            if header not in ['Connection', 'Keep-Alive',
                    'Content-Length', 'Transfer-Encoding', 'Content-Encoding']:
                django_response.__setitem__(header, response.headers[header])
                return django_response
