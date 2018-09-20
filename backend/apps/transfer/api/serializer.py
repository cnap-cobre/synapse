from rest_framework import serializers
from apps.transfer.models import TransferBatch, TransferFile


class TransferBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferBatch
        fields = ('id', 'user', 'dateInitiated')