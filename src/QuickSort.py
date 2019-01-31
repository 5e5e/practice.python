class QuickSort:
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def partition(self, arr, low, high):
        pivot = arr[int((low + high) / 2)]
        while True:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1

            if low < high:
                self.swap(arr, low, high)
            else:
                return high

    def quick_sort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quick_sort(arr, low, p)
            self.quick_sort(arr, p + 1, high)
