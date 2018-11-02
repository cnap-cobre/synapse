from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import TransferBatch, TransferFile
from apps.transfer.file_tasks import filePendingToDownloading
from apps.transfer.directory_tasks import expandDirectoryListing

# Trigger processing when TransferFile object is created
@receiver(post_save, sender=TransferFile)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        pathTokens = instance.fromPath.split('/')
        if pathTokens[-1] == '':
            # We have a directory path
            expandDirectoryListing.delay(instance.id)
        else:
            # We have a file path
            filePendingToDownloading.delay(instance.id)