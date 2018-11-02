from celery import shared_task
from .models import TransferBatch, TransferFile

@shared_task(bind=True, time_limit=90, default_retry_delay=10, max_retries=5)
def expand_directory_listing(self, fileId):
    # This MUST be idempotent
    file = TransferFile.objects.get(id=fileId)
    print("Directory FROM PATH: %s" % file.fromPath)
    adapter = file.get_from_adapter()
    file.status = 'ED'
    file.save()

    if self.request.retries == 0:
        create_target_directory.delay(fileId)

    try:
        directory_listing = adapter.list_directory(file.fromPath, file.batch.user)

        # Download the files
        for childFromPath in directory_listing['files']:
            childToPath = '/'.join(file.toPath.split('/')[0:-1] + childFromPath.split('/')[-1:])
            print("From Path %s .... To Path %s" % (childFromPath, childToPath))
            TransferFile.objects.create(
                batch=file.batch,
                fromPath=childFromPath,
                toPath=childToPath
            )
            # Make this idempotent (soon)

        # Expand the directories and eventually download their contents
        for childDirFromPath in directory_listing['directories']:
            childDirToPath = '/'.join(file.toPath.split('/')[0:-1] + childDirFromPath.split('/')[-2:])
            print("FROM DIR Path %s ... TO DIR Path %s" % (childDirFromPath, childDirToPath))
            TransferFile.objects.create(
                batch=file.batch,
                fromPath=childDirFromPath,
                toPath=childDirToPath
            )
            # Make this idempotent (soon)

        file.status = 'CP'
        file.save()
    except:
        print("Directory listing error occurred %d" % fileId)
        import traceback
        traceback.print_exc()
        self.retry(countdown=10)
        raise

@shared_task(bind=True, time_limit=30, default_retry_delay=5, max_retries=3)
def create_target_directory(self, fileId):
    file = TransferFile.objects.get(id=fileId)
    print("Create directory TO PATH: %s" % file.toPath)
    adapter = file.get_to_adapter()

    try:
        adapter.create_directory(file.toPath, file.batch.user)
    except:
        import traceback
        traceback.print_exc()
        self.retry()