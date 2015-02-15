from unittest2 import TestCase
from design_of_programs.exam import bowling

__author__ = 'Girish'



class Test(TestCase):

    def test1(self):
        self.assertEqual( bowling.bowling([1] * 20),20)
    def test2(self):
        self.assertEqual( bowling.bowling([4] * 20),80)
    def test3(self):
        self.assertEqual(bowling.bowling([9,1] * 10 + [9]),190)


