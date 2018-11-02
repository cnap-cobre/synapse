from rest_framework import viewsets
from apps.transfer.models import TransferBatch, TransferFile
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import HttpResponse

from ..dropbox_adapter import DropboxAdapter
from ..agave_adapter import AgaveAdapter

from .permissions import IsNotAllowed, IsTargetUser
from .serializer import TransferBatchSerializer


class TransferBatchViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = TransferBatch.objects.all().order_by('user')
    serializer_class = TransferBatchSerializer

    def get_permission(self):
        print("action", self.action)
        if self.action in ['update', 'partial_update', 'delete']:
            return IsNotAllowed()
        elif self.action in ['retrieve', 'create']:
            return IsTargetUser()
        elif self.action in ['list', 'metadata']:
            return IsAuthenticated()
        else:
            return IsNotAllowed()
