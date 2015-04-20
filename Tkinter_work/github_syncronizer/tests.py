from git.remote import Remote

__author__ = 'Girish'

import unittest

import git
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.repo = git.Repo("C:\\Users\\Girish\\Documents\\GitHub\\c_and_c++ Programs")
    def test_something(self):

        print(self.repo.remotes[0])


if __name__ == '__main__':
    unittest.main()
