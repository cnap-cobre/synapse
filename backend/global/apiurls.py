from django.urls import include, path, re_path
from django.conf.urls import url
from rest_framework import routers
from apps.user.views import UserViewSet
from apps.profile.views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls))
]
