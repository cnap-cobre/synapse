from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
import hashlib

class TransferBatch(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateInitiated = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=8, unique=True, default=None)

    def save(self, *args, **kwargs):
        if self.hash is None:
            self.hash = hashlib.sha256(str(user) + str(datetime.now())).hexdigest()[0:8]
        super().save(*args, **kwargs)


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