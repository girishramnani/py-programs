__author__ = 'Girish'

import unittest

from pell_solution import pell_coefficient
class MyTestCase(unittest.TestCase):
    def test_pells(self):
        self.assertEqual(pell_coefficient(19),[2,1,3,1,2,8])

if __name__ == '__main__':
    unittest.main()
