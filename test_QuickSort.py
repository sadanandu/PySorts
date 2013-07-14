from unittest import SkipTest, TestCase, main
import random
from QuickSort import *

class QuickSortTest(TestCase):

    def setUp(self):
        self.array = list()
        for item in xrange(20):
            self.array.append(random.randint(1,1000))
        self.inputArray = self.array[:]

    def test_QuickSortStable(self):
        self.assertEqual(QuickSortStable(self.inputArray[:]), sorted(self.inputArray))

    def test_QuickSortFirstElementPivot(self):
        QuickSortFirstElementPivot(self.inputArray, 0, len(self.inputArray) -1 )
        self.assertEqual(self.inputArray, sorted(self.array))

    def test_QuickSortMedianPivot(self):
        QuickSortMedainPivot(self.inputArray, 0, len(self.inputArray) -1 )
        self.assertEqual(self.inputArray, sorted(self.array))

if __name__ == '__main__':
    main()
