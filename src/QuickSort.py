import unittest

array0 = []
sorted_array0 = []
array1 = [1]
sorted_array1 = [1]
array2 = [6, 4, 1, 8, 9, 2, 7, 5, 3]
sorted_array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array3 = [6, 4, 2, 10, 9, 1, 7, 11, 5, 3, 0, 8]
sorted_array3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, low, high):
    pivot = arr[int((low + high) / 2)]
    i = low
    j = high
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            swap(arr, i, j)
        else:
            return j


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)
    return arr


class TestQuickSort(unittest.TestCase):
    def test_quick_sort0(self):
        self.assertEqual(quick_sort(array0, 0, array0.__len__() - 1), sorted_array0)

    def test_quick_sort1(self):
        self.assertEqual(quick_sort(array1, 0, array1.__len__() - 1), sorted_array1)

    def test_quick_sort2(self):
        self.assertEqual(quick_sort(array2, 0, array2.__len__() - 1), sorted_array2)

    def test_quick_sort3(self):
        self.assertEqual(quick_sort(array3, 0, array3.__len__() - 1), sorted_array3)


if __name__ == '__main__':
    unittest.main()
