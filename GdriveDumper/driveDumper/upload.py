from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

class UndefinedRoot(Exception):
    def __init__(self):
        super(Exception,self).__init__("So root folder defined")


class DriveUploader(object):
    def __init__(self, auth_file=None, root_folder=None):
        self.auth_file = auth_file
        self.root_folder = root_folder
        if not self.root_folder:
            self.create_folder = self._create_folder
        else:
            self.create_root_folder()

    @property
    def drive(self):

        try:
            return self._drive
        except:
            if self.auth_file:
                gauth = GoogleAuth(self.auth_file)
            else:
                gauth = GoogleAuth()
                gauth.LocalWebserverAuth()
                self._drive = GoogleDrive(gauth)
                return self._drive

    def create_root_folder(self):

        if self.root_folder:
            self.root_id = self._create_folder(self.root_folder)
            self.create_folder = self._create_folder_inside_root
        else:
            raise UndefinedRoot

    def _create_folder(self, name, parent=None):
        drive = self.drive
        json = {'title': name,
                'mimeType': 'application/vnd.google-apps.folder'}
        if parent:
            json['parents'] = [{'id': parent}]
        folder = drive.CreateFile(json)
        folder.Upload()
        return folder['id']

    def _create_folder_inside_root(self, name, parent=None):
        """
        creates a folder and returns the id of that folder
        """

        # maybe the drive wouldnt be initialed so better use the method
        return self._create_folder(parent=self.root_id)

    def create_file(self, file_location,parent=None):
        """
        create a file in parent directory , if not specified creates it in to root

        :param file_location:
        :return:
        """
        filename = file_location.split(os.sep)[-1]
        json = {
            'title':filename,
        }
        if parent:
            json['parents']=[{
                'id':parent
            }]
        file = self.drive.CreateFile()
        file.SetContentFile(file_location)
        file.Upload()
        return file['id']


