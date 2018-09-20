from allauth.socialaccount.models import SocialAccount, SocialToken
from agavepy.agave import Agave
import os
from django.conf import settings

class AgaveAdapter():
    def download(self, localPath, remotePath, user, uniqueBatchId):
        token_query = user.profile.tokens.filter(app__provider='agave')

        if not token_query.exists():
            raise PermissionDenied('No agave token found.')

        token = token_query.get().token

        systemId = remotePath.split('/')[1]
        remoteFilePath = '/'.join(remotePath.split('/')[2:])
        downloadDirectory = '/transient/%s/' % uniqueBatchId
        fullLocalPath = downloadDirectory + localPath

        if not os.path.exists(downloadDirectory):
            os.makedirs(downloadDirectory)

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

        systemId = remotePath.split('/')[1]
        remoteFilePath = '/'.join(remotePath.split('/')[2:])
        fullLocalPath = '/transient/%s/' % uniqueBatchId + localPath
        print(remoteFilePath)

        ag = Agave(api_server=settings.API_BASE_URL_AGAVE, token=token)
        f = open(fullLocalPath, 'rb')
        response = ag.files.importData(filePath='' + remoteFilePath, systemId=systemId, fileToUpload=f)
        print(response)
        f.close()