from django.urls import include, path, re_path
from django.conf.urls import url
from rest_framework import routers

from apps.profile.views import ProfileViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
]
