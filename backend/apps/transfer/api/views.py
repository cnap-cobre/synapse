from rest_framework import viewsets
from apps.transfer.models import TransferBatch, TransferFile
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import HttpResponse

from ..dropbox_adapter import DropboxAdapter
from .serializer import TransferBatchSerializer

class TransferBatchViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = TransferBatch.objects.all().order_by('user')
    serializer_class = TransferBatchSerializer

    @action(methods=['get'], detail=False)
    def dropbox_adapter_testing(self, request):
        print(request)
        print(request.path)
        dba = DropboxAdapter()
        #dba.download('/synapse-logo.png', '/synapse-logo.png', request.user, 'a134radfpizza')
        #dba.upload('/easy-eagle-dvd-with-audiio-0.mp4', '/airplane/easy-eagle-dvd-with-audio-0.mp4', request.user, 'pizza')
        return HttpResponse('ASDF')