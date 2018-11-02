from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import TransferBatch, TransferFile
from apps.transfer.file_tasks import filePendingToDownloading

@receiver(post_save, sender=TransferFile)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        # Trigger processing when TransferFile object is created
        print("File transfer object was created!")
        filePendingToDownloading.delay(instance.id)