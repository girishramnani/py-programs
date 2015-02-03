__author__ = 'Girish'

import unittest
from design_of_programs.poker import poker

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.fk ="6S 6C 6H 6D 9H".split()
        self.sf ="1C 2C 3C 4C 5C".split()
        self.fh ="TD TC TH 7C 7D".split()
    def test_something(self):
        self.assertEqual(poker.rank([self.fk,self.sf,self.fh]), self.sf)

    def test_2(self):
        self.assertEqual(poker.rank([self.fk,self.fk]),self.fk)
    def test_3(self):
        self.assertEqual(poker.rank([self.sf,self.fh]),self.sf)
    def test_4(self):
        self.assertEqual(poker.rank([self.sf]),self.sf)



if __name__ == '__main__':
    unittest.main()
