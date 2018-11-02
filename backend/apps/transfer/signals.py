from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import TransferBatch, TransferFile
from apps.transfer.file_tasks import file_pending_to_downloading
from apps.transfer.directory_tasks import expand_directory_listing

# Trigger processing when TransferFile object is created
@receiver(post_save, sender=TransferFile)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        pathTokens = instance.fromPath.split('/')
        if pathTokens[-1] == '':
            # We have a directory path
            expand_directory_listing.delay(instance.id)
        else:
            # We have a file path
            file_pending_to_downloading.delay(instance.id)