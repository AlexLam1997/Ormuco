from Q1Overlap import Overlap
from unittest import TestCase

class OverlapTest(TestCase):

    def test_SimpleNoOverlap(self):
        hasOverlap = Overlap.isOverlapping(1,2, 3, 4)
        self.assertEqual(hasOverlap, False)

    def test_HardNoOverlap(self):
        hasOverlap = Overlap.isOverlapping(5, 1, 8, 7)
        self.assertEqual(hasOverlap, False)

    def test_SimpleWithOverlap(self):
        hasOverlap = Overlap.isOverlapping(3,7,1,4)
        self.assertEqual(hasOverlap, True)

    def test_HardWithOverlap(self):
        hasOverlap = Overlap.isOverlapping(10,5,6,1)
        self.assertEqual(hasOverlap, True)

    def test_OverlapEdgeEquality(self):
        hasOverlap = Overlap.isOverlapping(1,3, 3, 4)
        self.assertEqual(hasOverlap, True)

    def test_HardOverlapEdgeEquality(self):
        hasOverlap = Overlap.isOverlapping(3,1, 4, 3)
        self.assertEqual(hasOverlap, True)

    def test_HardOverlapZeros(self):
        hasOverlap = Overlap.isOverlapping(0,0, 0, 0)
        self.assertEqual(hasOverlap, True)




