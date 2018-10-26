from celery import shared_task
from .models import TransferBatch, TransferFile

@shared_task
def filePendingToDownloading(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'DL'
    file.save()
    print("File Pending and downloading now")
    print("To Path:", file.toPath)
    print("From Path:", file.fromPath)

    try:
        file.download()
        fileDownloadingToDownloadSucceeded.delay(fileId)
    except ValueError:
        print("Provider not matched on download.")
        fileDownloadingToDownloadFailed.delay(fileId)
    except:
        print("Some fatal error occurred")
        import traceback
        traceback.print_exc()
        fileDownloadingToDownloadFailed.delay(fileId)

@shared_task
def fileDownloadingToDownloadSucceeded(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'DS'
    file.save()
    print("file DL succeeded: ", file.fromPath)

    fileDownloadSucceededToUploading.delay(fileId)

@shared_task
def fileDownloadingToDownloadFailed(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'DF'
    file.save()
    print("file DL failed: ", file.fromPath)

    #filePendingToDownloading.delay(fileId)

@shared_task
def fileDownloadSucceededToUploading(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'UP'
    file.save()
    print("Currently uploading to: ", file.toPath)

    try:
        file.upload()
        fileUploadingToUploadSucceeded.delay(fileId)
    except ValueError:
        print("Provider not matched on upload.")
        fileUploadingToUploadFailed.delay(fileId)
    except:
        print("Some fatal error occurred")
        import traceback
        traceback.print_exc()
        fileUploadingToUploadFailed.delay(fileId)

@shared_task
def fileUploadingToUploadFailed(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'UF'
    file.save()
    print("file UP failed: ", file.toPath)

    # fileDownloadSucceededToUploading.delay(fileId)

@shared_task
def fileUploadingToUploadSucceeded(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'US'
    file.save()
    print("file UP succeeded: ", file.toPath)

    fileUploadSucceededToComplete.delay(fileId)

@shared_task
def fileUploadSucceededToComplete(fileId):
    file = TransferFile.objects.get(id=fileId)
    file.status = 'CP'
    file.save()
    print("file transfer complete!!!")
    print("file was transfered from %s to %s" % (file.fromPath, file.toPath))



@shared_task
def launchBatchTransfers():
    # In the future, we should likely limit the number of simultaneous file transfers
    # For now, we will simply launch them all.
    singleFile = TransferFile.objects.filter(status='PD').all()[0]
    filePendingToDownloading.delay(singleFile.id)