__author__ = 'Girish'

import unittest
from design_of_programs.poker import poker

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.fk ="6S 6C 6H 6D 9H".split()
        self.sf ="1C 2C 3C 4C 5C".split()
        self.fh="TD TC TH 7C 7D".split()
        self.tp="5S 5D 9H 9C 6S".split()
        self.fh="TD TC TH 7C 7D".split()
        self.s1 ="AS 2S 3S 4S 5C".split() # Straight
        self.s2 ="2C 3C 4C 5S 6S".split() #straight
        self.ah ="AS 2S 3S 4S 6C".split()
        self.sh ="2S 3S 4S 6C 7D".split()
        self.assertEqual(poker.card_ranks(self.fk),[9,6,6,6,6])
    def test_exceptional(self):
        self.assertEqual(poker.rank([self.s1,self.s2,self.ah,self.sh]),self.s2)
    def test_tie(self):
        self.assertEqual(poker.rank([self.fk,self.fk]),[self.fk,self.fk])
    def test_3(self):
        self.assertEqual(poker.rank([self.sf,self.fh]),self.sf)
    def test_4(self):
        self.assertEqual(poker.rank([self.sf]),self.sf)
    def test_5(self):
        self.assertEqual(poker._hand_rank(self.sf),(8,5))
    def test_card_rank_1(self):
        self.assertEqual(poker.card_ranks(self.sf),[5,4,3,2,1])
    def test_straight(self):
        self.assertEqual(poker.straight([9,8,7,6,5]),True)
    def test_flush(self):
        self.assertEqual(poker.flush(self.sf),True)
    def test_kind(self):
        self.assertEqual(poker.kind(2,poker.card_ranks(self.fh)),7)
    def test_3_kind(self):
        self.assertEqual(poker.kind(3,poker.card_ranks(self.fh)),10)
    def test_wrong_kind(self):
        self.assertEqual(poker.kind(1,poker.card_ranks(self.fh)),None)
    def test_two_pairs(self):
        self.assertEqual(poker.two_pair(poker.card_ranks(self.tp)),[9,5])
    def test_wrong_two_pairs(self):
        self.assertEqual(poker.two_pair(poker.card_ranks(self.sf)),None)

if __name__ == '__main__':
    unittest.main()
