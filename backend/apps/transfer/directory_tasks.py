from celery import shared_task
from .models import TransferBatch, TransferFile


@shared_task(bind=True, time_limit=60, default_retry_delay=10, max_retries=3)
def expand_directory_listing(self, fileId):
    # This MUST be idempotent
    print("THIS IS A DIRECTORY!!!!!")
    pass
