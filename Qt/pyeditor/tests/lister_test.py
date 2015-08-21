__author__ = 'Girish'

import file_to_list as fl
import unittest2
class test(unittest2.TestCase):
    def setUp(self):
        self.lister = fl.Lister()
    def test_constructor(self):
        self.assertEqual(self.lister.location,"C:\\Users\\Girish\\PycharmProjects\\pyeditor\\words.txt")
