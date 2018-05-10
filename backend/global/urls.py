"""dms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from apps.main import views as main_views
from apps.agave_proxy.views import AgaveProxy
from apps.dropbox_proxy.views import DropboxProxy, \
        DropboxApiProxy, DropboxContentProxy

urlpatterns = [
    path('', main_views.app),
    path('admin/', admin.site.urls),
    path('accounts/profile/', include('apps.profile.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^agave/', AgaveProxy.as_view(
        url_name='agpx'
    ), name='agpx'),
    re_path(r'^dropbox/api/', DropboxApiProxy.as_view(
        url_name='dbapipx'
    ), name='dbapipx'),
    re_path(r'^dropbox/content/', DropboxContentProxy.as_view(
        url_name='dbcontentpx'
    ), name='dbcontentpx'),
    re_path(r'^dropbox/', DropboxProxy.as_view(
        url_name='dbpx'
    ), name='dbpx'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [url(r'^__debug__/', include(debug_toolbar.urls))] \
        + urlpatterns \
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
