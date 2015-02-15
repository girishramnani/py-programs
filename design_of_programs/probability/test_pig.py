from design_of_programs.probability.pig import hold, roll, State

__author__ = 'Girish'



import unittest2

class testing(unittest2.TestCase):
    def setUp(self):

        self.s=State(0,10,20,30)
    def test_hold(self):
        self.assertEqual(hold(self.s),State(1,20,40,0))
    def test_rool(self):
        self.assertEqual(roll(self.s,6),State(0,10,20,36))
