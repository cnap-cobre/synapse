from allauth.socialaccount.models import SocialAccount, SocialToken
from agavepy.agave import Agave
import os
from django.conf import settings
from django.core.exceptions import PermissionDenied

class AgaveAdapter():
    def download(self, localPath, remotePath, user, uniqueBatchId):
        token_query = user.profile.tokens.filter(app__provider='agave')

        if not token_query.exists():
            raise PermissionDenied('No agave token found.')

        token = token_query.get().token

        systemProvider = remotePath.split('/')[1]
        systemId = remotePath.split('/')[2]
        remoteFilePath = '/'.join([''] + remotePath.split('/')[3:])
        downloadDirectory = '/transient/%s/' % uniqueBatchId
        fullLocalPath = downloadDirectory + localPath

        if not os.path.exists(downloadDirectory):
            os.makedirs(downloadDirectory)

        fullLocalDir = '/'.join(fullLocalPath.split('/')[0:-1] + [''])
        if not os.path.exists(fullLocalDir):
            os.makedirs(fullLocalDir, mode=0o755, exist_ok=True)

        ag = Agave(api_server=settings.API_BASE_URL_AGAVE, token=token)
        response = ag.files.download(filePath=remoteFilePath, systemId=systemId)
        f = open(fullLocalPath, 'wb')
        f.write(response.content)
        f.close()


    def upload(self, localPath, remotePath, user, uniqueBatchId):
        token_query = user.profile.tokens.filter(app__provider='agave')

        if not token_query.exists():
            raise PermissionDenied('No agave token found.')

        token = token_query.get().token

        systemProvider = remotePath.split('/')[1]
        systemId = remotePath.split('/')[2]
        remoteFilePath = '/'.join([''] + remotePath.split('/')[3:-1])
        fullLocalPath = '/transient/%s/' % uniqueBatchId + localPath

        ag = Agave(api_server=settings.API_BASE_URL_AGAVE, token=token)
        f = open(fullLocalPath, 'rb')
        response = ag.files.importData(filePath='' + remoteFilePath, systemId=systemId, fileToUpload=f)
        f.close()