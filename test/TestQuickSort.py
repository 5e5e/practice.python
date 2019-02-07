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
array4 = [1, 5, 5, 5, 5, 5, 1, 2, 5]
sorted_array4 = [1, 1, 2, 5, 5, 5, 5, 5, 5]
array5 = [5, 5, 5, 5, 5, 5, 5, 5, 5]
sorted_array5 = [5, 5, 5, 5, 5, 5, 5, 5, 5]


class TestQuickSort(unittest.TestCase):

    def test_quick_sort0(self):
        quick_sort = QuickSort()
        quick_sort.sort1(array0, 0, array0.__len__() - 1)
        self.assertEqual(sorted_array0, array0)

    def test_quick_sort1(self):
        quick_sort = QuickSort()
        quick_sort.sort1(array1, 0, array1.__len__() - 1)
        self.assertEqual(sorted_array1, array1)

    def test_quick_sort2(self):
        quick_sort = QuickSort()
        quick_sort.sort2(array2, 0, array2.__len__() - 1)
        self.assertEqual(sorted_array2, array2)

    def test_quick_sort3(self):
        quick_sort = QuickSort()
        quick_sort.sort1(array3, 0, array3.__len__() - 1)
        self.assertEqual(sorted_array3, array3)

    def test_quick_sort4(self):
        quick_sort = QuickSort()
        quick_sort.sort1(array4, 0, array4.__len__() - 1)
        self.assertEqual(sorted_array4, array4)

    def test_quick_sort5(self):
        quick_sort = QuickSort()
        quick_sort.sort2(array5, 0, array5.__len__() - 1)
        self.assertEqual(sorted_array5, array5)


if __name__ == '__main__':
    unittest.main()
