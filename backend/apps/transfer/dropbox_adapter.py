from allauth.socialaccount.models import SocialAccount, SocialToken
import dropbox
import os


class DropboxAdapter():
    def download(self, localPath, remotePath, user, uniqueBatchId):
        token_query = user.profile.tokens.filter(app__provider='dropbox')

        if not token_query.exists():
            raise PermissionDenied('No dropbox token found.')

        token = token_query.get().token

        downloadDirectory = '/transient/%s/' % uniqueBatchId
        basename = os.path.basename(remotePath)
        fullLocalPath = downloadDirectory + basename

        if not os.path.exists(downloadDirectory):
            os.makedirs(downloadDirectory)

        dbx = dropbox.Dropbox(token)
        dbx.files_download_to_file(fullLocalPath, remotePath)
        print(dbx.users_get_current_account())


    def upload(self, localPath, remotePath, user, uniqueBatchId):
        token_query = user.profile.tokens.filter(app__provider='dropbox')

        if not token_query.exists():
            raise PermissionDenied('No dropbox token found.')

        token = token_query.get().token
        dbx = dropbox.Dropbox(token)

        basename = os.path.basename(localPath)
        localDirectory = '/transient/%s/' % uniqueBatchId
        fullLocalPath = localDirectory + basename

        file_size = os.path.getsize(fullLocalPath)
        CHUNK_SIZE = 4 * 1024 * 1024

        f = open(fullLocalPath, "rb")

        if file_size <= CHUNK_SIZE:
            dbx.files_upload(f.read(), remotePath)
        else:
            upload_session = dbx.files_upload_session_start(f.read(CHUNK_SIZE))
            cursor = dropbox.files.UploadSessionCursor(session_id=upload_session.session_id, offset=f.tell())
            commit = dropbox.files.CommitInfo(path=remotePath)

            while f.tell() < file_size:
                if (file_size - f.tell()) <= CHUNK_SIZE:
                    dbx.files_upload_session_finish(f.read(CHUNK_SIZE), cursor, commit)
                else:
                    dbx.files_upload_session_append(f.read(CHUNK_SIZE), cursor.session_id, cursor.offset)
                    cursor.offset = f.tell()
                    print(cursor.offset)

        f.close()