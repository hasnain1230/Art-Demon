import io
import pickle
import os.path
import json
import sys

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
from googleapiclient.http import MediaIoBaseDownload

import os


# Client authorizes.
# All file names and file IDs are queued for downloads in file list stored in memory.
# Those file IDs are stored to already downloaded file, downloaded.json. These files are assumed to have been downloaded
# Downloaded files are stored. When function is called again, it will search to see if there are any new files,

class Drive:
    service = None
    SCOPES = ['https://www.googleapis.com/auth/drive']
    DOWNLOAD_LOCATION = '../assets/Palettes/'
    downloaded_files = set()

    @classmethod
    def auth(cls):
        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        creds = None
        if os.path.exists('utilities/token.pickle'):
            with open('utilities/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'utilities/credentials.json', cls.SCOPES)
                flow.authorization_url(access_type='offline', include_granted_scopes='true')
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('utilities/token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        cls.service = build('drive', 'v3', credentials=creds)

    def get_files_from_id(self, folder_id):
        page_token = None
        downloaded = open('assets/Palettes/downloaded.json',
                          'w+')  # This is to log the most recent files that have been downloaded.
        response = self.service.files().list(q=f"'{folder_id}' in parents", spaces='drive',
                                             fields='nextPageToken, files(id, name)',
                                             pageToken=page_token).execute()
        downloaded.write(json.dumps(response.get('files'), indent=4))

        downloaded.close()

    def download_files_from_json(self, json_file):
        file_ids = []
        file_names = []  # Memory could be saved here, but for ease, I decided against it.
        count = 0

        with open(json_file, 'r') as jf:
            json_data = json.load(jf)

            for data in json_data:
                file_ids.append(data.get('id'))
                file_names.append(data.get('name'))

            jf.close()
        if len(file_ids) == len(file_names):
            # Everything above could have been done here, but it would have been less time efficient.
            # This might be slightly less memory efficient, but it's better on the time efficiency.
            for ids in range(len(file_ids)):
                file_id = file_ids[ids]
                path = 'assets/Palettes/%s' % file_names[ids]

                if os.path.exists(path):
                    continue

                # print('File ID Being Downloaded (Maybe)? {}' % file_id)
                request = self.service.files().get_media(fileId=file_id)

                fh = io.BytesIO()
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    count += 1
                    print(f'Downloading file ID : Name ~ {file_ids[ids]} : {file_names[ids]}')

                fh.seek(0)
                with open(path, 'wb') as f:
                    f.write(fh.getbuffer())  # Warning can be ignored.
                    f.close()

        else:
            raise Exception('File IDs and name are not same in quantity.')