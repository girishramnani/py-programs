import unittest
from unittest import TestCase
from upload import DriveUploader

class DriveUploaderTests(TestCase):


    def setUp(self):
        self.drive = DriveUploader()


    def test_create_folder(self):
        self.folder_id = self.drive.create_folder("girishramnani")
        file_list = self.drive.drive.ListFile({'q':"title='girishramnani'"}).GetList()
        file = file_list[0]
        self.assertEquals(file['id'],self.folder_id)

    def test_create_file(self):
        id = self.drive.create_file("cli.py")
        file_list = self.drive.drive.ListFile({'q':"title='cli.py'"}).GetList()
        self.assertEquals(id,file_list[0]['id'])

if __name__ =="__main__":
    unittest.main()
