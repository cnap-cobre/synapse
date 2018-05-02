from django.urls import path
from . import views

urlpatterns = [
    path('', views.react_browse, name="browse"),
]
