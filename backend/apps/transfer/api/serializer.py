from rest_framework import serializers
from apps.transfer.models import TransferBatch, TransferFile


class TransferFileSerializer(serializers.ModelSerializer):
    fromPath = serializers.CharField()
    toPath = serializers.CharField()

    class Meta:
        model = TransferFile
        fields = ('id', 'fromPath', 'toPath', 'status')


class TransferBatchSerializer(serializers.ModelSerializer):
    files = TransferFileSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TransferBatch
        fields = ('id', 'user', 'dateInitiated', 'files')

    def create(self, validated_data):
        print(validated_data)
        files_data = validated_data.pop('files')
        batch = TransferBatch.objects.create(**validated_data)
        for file_data in files_data:
            print("file_data", file_data)
            TransferFile.objects.create(batch=batch, **file_data)
        return batch