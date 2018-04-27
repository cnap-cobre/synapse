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
from apps.accounts import views as account_views
from apps.agave_proxy.views import AgaveProxy

urlpatterns = [
    path('', main_views.home_page),
    path('admin/', admin.site.urls),
    path('accounts/profile/', account_views.UserProfileView.as_view()),
    path('accounts/', include('allauth.urls')),
    path('browse/', include('apps.browse.urls')),
    re_path(r'^agave/', AgaveProxy.as_view(
        base_url=settings.API_BASE_URL_AGAVE,
        url_name='agpx'
    ), name='agpx'),
    #path('dropbox/', DropboxyHttpProxy.as_view(base_url=settings.API_BASE_URL_DROPBOX)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + \
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
