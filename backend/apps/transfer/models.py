from django.contrib.auth.models import User
from django.db import models


class TransferBatch(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateInitiated = models.DateTimeField(auto_now_add=True)


class TransferFile(models.Model):
    STATUS_CHOICES = (
        ('QD', 'queued'),
        ('DL', 'downloading'),
        ('DF', 'download failed'),
        ('UP', 'uploading'),
        ('UF', 'upload failed'),
        ('CP', 'complete')
    )

    batch = models.ForeignKey('TransferBatch', on_delete=models.CASCADE)
    status = models.CharField(
        default='QD',
        choices=STATUS_CHOICES,
        max_length=2
    )
    fromPath = models.CharField(max_length=500)
    toPath = models.CharField(max_length=500)