__author__ = 'Girish'

import unittest
from design_of_programs.poker import poker

class MyTestCase(unittest.TestCase):

    def test_something(self):
        fk ="6S 6C 6H 6D 9H".split()
        sf ="1C 2C 3C 4C 5C".split()
        fh ="TD TC TH 7C 7D".split()
        print(fk)

        self.assertEqual(poker.rank([fk,sf,fh]), sf)


if __name__ == '__main__':
    unittest.main()
