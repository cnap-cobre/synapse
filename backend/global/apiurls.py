from django.urls import include, path, re_path
from django.conf.urls import url
from rest_framework import routers
from apps.user.api.views import UserViewSet, GroupViewSet
from apps.profile.api.views import ProfileViewSet
from apps.transfer.api.views import TransferBatchViewSet

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'transfer_batches', TransferBatchViewSet)

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^rest-auth/', include('apps.accounts.urls')),
    url(r'^', include(router.urls))
]
