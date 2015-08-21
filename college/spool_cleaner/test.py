__author__ = 'Girish'
import unittest
from unittest import TestCase
from college.spool_cleaner.app import SpoolCleaner
from filecmp import cmp
import os
import glob

def cmp2(path1,path2):
    return cmp(os.path.abspath(path1),os.path.abspath(path2))

class SpoolTest(TestCase):
    def test_contructor(self):
        spool_cleaner = SpoolCleaner("data/input01.txt")

    def test_compare_files(self):
        self.assertEqual(cmp2("data/compare1","data/compare2"),True)

    def test_spool1(self):
        IND =1
        spool_cleaner = SpoolCleaner("data/input{}.txt".format(IND))
        spool_cleaner.clean("data/output{}.txt".format(IND))
        self.assertEqual(cmp2("data/output{}.txt".format(IND),"data/cleaned{}.txt".format(IND)),True)

    def test_spool2(self):
        IND =2
        spool_cleaner = SpoolCleaner("data/input{}.txt".format(IND))
        spool_cleaner.clean("data/output{}.txt".format(IND))
        self.assertEqual(cmp2("data/output{}.txt".format(IND),"data/cleaned{}.txt".format(IND)),True)



    def tearDown(self):
        for file in glob.glob("data/output*"):
            os.remove(file)


if __name__ =='__main__':
    unittest.main()