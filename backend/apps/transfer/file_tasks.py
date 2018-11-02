from celery import shared_task
from .models import TransferBatch, TransferFile


@shared_task(bind=True, time_limit=600, default_retry_delay=30, max_retries=3)
def file_pending_to_downloading(self, fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'DL'
    file.save()
    print("File Pending and downloading now %d" % fileId)

    try:
        file.download()
        file_downloading_to_download_succeeded.delay(fileId)
    except ValueError:
        print("Provider not matched on download.  %d" % fileId)
        file_downloading_to_download_failed.delay(fileId)
        raise
    except:
        print("Some fatal error occurred %d" % fileId)
        import traceback
        traceback.print_exc()
        file_downloading_to_download_failed.delay(fileId)
        self.retry(countdown=10)
        raise


@shared_task
def file_downloading_to_download_succeeded(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'DS'
    file.save()
    print("file DL succeeded %d" % fileId)

    file_download_succeeded_to_uploading.delay(fileId)


@shared_task
def file_downloading_to_download_failed(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'DF'
    file.save()
    print("file DL failed %d" % fileId)


@shared_task(bind=True, time_limit=600, default_retry_delay=30, max_retries=3)
def file_download_succeeded_to_uploading(self, fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'UP'
    file.save()
    print("Currently uploading to %d" % fileId)

    try:
        file.upload()
        file_uploading_to_upload_succeeded.delay(fileId)
    except ValueError:
        print("Provider not matched on upload %d" % fileId)
        file_uploading_to_upload_failed.delay(fileId)
        raise
    except:
        print("Some fatal error occurred %d" % fileId)
        import traceback
        traceback.print_exc()
        file_uploading_to_upload_failed.delay(fileId)
        self.retry(countdown=10)
        raise


@shared_task
def file_uploading_to_upload_failed(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'UF'
    file.save()
    print("file UP failed %d" % fileId)


@shared_task
def file_uploading_to_upload_succeeded(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'US'
    file.save()
    file.cleanup()
    print("file UP succeeded %d" % fileId)

    file_upload_succeeded_to_complete.delay(fileId)


@shared_task
def file_upload_succeeded_to_complete(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'CP'
    file.save()
    print("file transfer complete!!! %d" % fileId)
    print("file was transfered from %s to %s" % (file.fromPath, file.toPath))
