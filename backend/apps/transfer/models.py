from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from .agave_adapter import AgaveAdapter
from .dropbox_adapter import DropboxAdapter

import hashlib
import os

class TransferBatch(models.Model):
    STATUS_CHOICES = (
        ('PD', 'pending'),
        ('RN', 'running'),
        ('ER', 'complete with errors'),
        ('CP', 'complete')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateInitiated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        default='PD',
        choices=STATUS_CHOICES,
        max_length=2
    )
    hash = models.CharField(max_length=8, unique=True, default=None)

    def save(self, *args, **kwargs):
        if self.hash is None:
            self.hash = hashlib.sha256((str(self.user) + str(datetime.now())).encode('utf-8')).hexdigest()[0:8]
        super().save(*args, **kwargs)


class TransferFile(models.Model):
    STATUS_CHOICES = (
        ('PD', 'pending'),
        ('DL', 'downloading'),
        ('DF', 'download failed'),
        ('DS', 'download succeeded'),
        ('UP', 'uploading'),
        ('UF', 'upload failed'),
        ('US', 'upload succeeded'),
        ('CP', 'complete')
    )

    # State transition table for files
    # PD => DL => DS => UP => US => CP
    # DL => DF => DL   (error condition)
    # UP => UF => UP   (error condition)

    # State transition table for directories
    #

    batch = models.ForeignKey('TransferBatch',
        on_delete=models.CASCADE,
        related_name='files'
    )
    status = models.CharField(
        default='PD',
        choices=STATUS_CHOICES,
        max_length=2
    )
    retries = models.PositiveIntegerField(default=0)
    fromPath = models.CharField(max_length=500)
    toPath = models.CharField(max_length=500)

    def get_from_adapter(self):
        from_tokens = self.fromPath.split('/')
        if from_tokens[1] == 'dropbox':
            return DropboxAdapter()
        elif from_tokens[1] == 'agave':
            return AgaveAdapter()
        else:
            raise ValueError

    def get_to_adapter(self):
        to_tokens = self.toPath.split('/')
        if to_tokens[1] == 'dropbox':
            return DropboxAdapter()
        elif to_tokens[1] == 'agave':
            return AgaveAdapter()
        else:
            raise ValueError

    def download(self):
        from_tokens = self.fromPath.split('/')
        local_path = '/'.join([''] + from_tokens[3:])
        adapter = self.get_from_adapter()
        adapter.download(
            local_path,
            self.fromPath,
            self.batch.user,
            self.batch.hash
        )

    def upload(self):
        from_tokens = self.fromPath.split('/')
        local_path = '/'.join([''] + from_tokens[3:])
        adapter = self.get_to_adapter()
        adapter.upload(
            local_path,
            self.toPath,
            self.batch.user,
            self.batch.hash
        )

    def cleanup(self):
        from_tokens = self.fromPath.split('/')
        localPath = '/'.join([''] + from_tokens[3:])
        fullLocalPath = '/transient/%s/' % self.batch.hash + localPath
        if os.path.exists(fullLocalPath):
            os.remove(fullLocalPath)