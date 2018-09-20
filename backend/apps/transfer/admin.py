from django.contrib import admin
from apps.transfer.models import TransferBatch, TransferFile

admin.site.register(TransferBatch)
admin.site.register(TransferFile)