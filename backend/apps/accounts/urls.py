from django.urls import include, path, re_path
from django.conf.urls import url
from rest_framework import routers


from allauth.socialaccount.providers.agave.views import AgaveAdapter
from allauth.socialaccount.providers.globus.views import GlobusAdapter
from allauth.socialaccount.providers.dropbox.views import DropboxOAuth2Adapter

from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView, SocialLoginView, SocialConnectView
)


class AgaveLogin(SocialLoginView):
    adapter_class = AgaveAdapter


class GlobusLogin(SocialLoginView):
    adapter_class = GlobusAdapter


class DropboxLogin(SocialLoginView):
    adapter_class = DropboxOAuth2Adapter


class AgaveConnect(SocialConnectView):
    adapter_class = AgaveAdapter


class GlobusConnect(SocialConnectView):
    adapter_class = GlobusAdapter


class DropboxConnect(SocialConnectView):
    adapter_class = DropboxOAuth2Adapter


urlpatterns = [
    url(r'^', include('rest_auth.urls')),
    url(r'^registration/', include('rest_auth.registration.urls')),

    url(
        r'^socialaccounts/$',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    url(
        r'^socialaccounts/(?P<pk>\d+)/disconnect/$',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    ),

    url(r'^agave/$', AgaveLogin.as_view(), name='agave_login'),
    url(r'^dropbox/$', DropboxLogin.as_view(), name='dropbox_login'),
    url(r'^globus/$', GlobusLogin.as_view(), name='globus_login'),

    url(r'^agave/connect/$', AgaveConnect.as_view(), name='agave_connect'),
    url(r'^dropbox/connect/$', DropboxConnect.as_view(), name='dropbox_connect'),
    url(r'^globus/connect/$', GlobusConnect.as_view(), name='globus_connect'),
]
