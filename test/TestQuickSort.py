import unittest

from src.QuickSort import QuickSort

array0 = []
sorted_array0 = []
array1 = [1]
sorted_array1 = [1]
array2 = [6, 4, 1, 8, 9, 2, 7, 5, 3]
sorted_array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array3 = [6, 4, 2, 10, 9, 1, 7, 11, 5, 3, 0, 8]
sorted_array3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


class TestQuickSort(unittest.TestCase):

    def test_quick_sort0(self):
        quick_sort = QuickSort()
        quick_sort.quick_sort(array0, 0, array0.__len__() - 1)
        self.assertEqual(array0, sorted_array0)

    def test_quick_sort1(self):
        quick_sort = QuickSort()
        quick_sort.quick_sort(array1, 0, array1.__len__() - 1)
        self.assertEqual(array1, sorted_array1)

    def test_quick_sort2(self):
        quick_sort = QuickSort()
        quick_sort.quick_sort(array2, 0, array2.__len__() - 1)
        self.assertEqual(array2, sorted_array2)

    def test_quick_sort3(self):
        quick_sort = QuickSort()
        quick_sort.quick_sort(array3, 0, array3.__len__() - 1)
        self.assertEqual(array3, sorted_array3)


if __name__ == '__main__':
    unittest.main()
