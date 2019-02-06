import unittest

from src.BubbleSort import BubbleSort

array0 = []
sorted_array0 = []
array1 = [1]
sorted_array1 = [1]
array2 = [6, 4, 1, 8, 9, 2, 7, 5, 3]
sorted_array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array3 = [6, 4, 2, 10, 9, 1, 7, 11, 5, 3, 0, 8]
sorted_array3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort_0(self):
        b = BubbleSort()
        b.sort(array0)
        self.assertEqual()


def test_bubble_sort_1(self):
    pass


def test_bubble_sort_2(self):
    pass


def test_bubble_sort_3(self):
    pass


if __name__ == '__main__':
    unittest.main()
