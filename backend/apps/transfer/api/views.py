from rest_framework import viewsets
from apps.transfer.models import TransferBatch, TransferFile
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import HttpResponse

from ..dropbox_adapter import DropboxAdapter
from ..agave_adapter import AgaveAdapter

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
        #dba.upload('/easy-eagle-dvd-with-audiio-1.mp4', '/airplane/easy-eagle-dvd-with-audio-1.mp4', request.user, 'pizza')
        return HttpResponse('ASDF')

    @action(methods=['get'], detail=False)
    def agave_adapter_testing(self, request):
        print(request)
        print(request.path)
        aga = AgaveAdapter()
        #aga.download('/example.c', '/beocat-please-work/homes/kmdice/BrownianSimple3d/00-omp-naive.cpp', request.user, 'blue3')
        aga.upload('testing123.txt', '/beocat-please-work/homes/kmdice/', request.user, 'blue4')
        return HttpResponse('ASDFASDF')