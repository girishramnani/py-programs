__author__ = 'Girish'
import math
"""maximum segment tree """

class SegmentTree(object):

    def __init__(self,li=[]):
        self._li = li
        self._ans_tree = [ -1 for _ in range(int(pow(2,(len(li)-1))))]
        if li:
            self._build_tree(0,len(li))

    def __str__(self):
        return "".join(["segTree ",str(self._li)])

    def _build_tree(self,low,high,index=0):
        if abs(low-high)==1:
            self._ans_tree[index]=low
            return
        self._build_tree(low,(low+high)//2,self.left(index))
        self._build_tree(((low+high)//2),high,self.right(index))
        self._ans_tree[index] = self._ans_tree[self.left(index)] if self._li[self._ans_tree[self.left(index)]] > self._li[self._ans_tree[self.right(index)]] else self._ans_tree[self.right(index)]

    def get_tree(self):
        return self._ans_tree
    def findmin(self,first,last):
        pass

    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def parent(self,i):
        return int(math.floor((i-1)/2))


import unittest

class tests(unittest.TestCase):
    def setUp(self):
        self.segTree = SegmentTree()

    def test_parent_left(self):
        for i in range(10):
            self.assertEqual(self.segTree.parent(self.segTree.left(i)),i)

    def test_parent_right(self):
        for i in range(10):
            self.assertEqual(self.segTree.parent(self.segTree.right(i)),i)

    def test_contructor(self):
        segTree = SegmentTree()
        self.assertEqual(segTree._li,[])

    def test_contrucor_noempty(self):
        segTree = SegmentTree([5,6,3,4,10])
        self.assertEqual(segTree._li,[5,6,3,4,10])

    def test_str(self):
        segTree = SegmentTree([5,6,3,4,10])
        self.assertEqual(str(segTree),"segTree [5, 6, 3, 4, 10]")

    def test_ansTree(self):
        segTree = SegmentTree([5,6,3,4,10])
        self.assertEqual(segTree.get_tree(),[4, 1, 4, 0, 1, 2, 4, -1, -1, -1, -1, -1, -1, 3, 4,-1])

if __name__=="__main__":
    unittest.main()
