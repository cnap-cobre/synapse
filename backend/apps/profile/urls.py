from django.urls import include, path, re_path
from django.conf.urls import url
from . import views as profile_views

urlpatterns = [
    re_path(r'^add_beocat.sh', profile_views.add_beocat_script)
]
