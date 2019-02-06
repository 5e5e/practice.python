class QuickSort:
    def sort1(self, arr, low, high):
        if low < high:
            p = self.partition1(arr, low, high)
            self.sort1(arr, low, p)
            self.sort1(arr, p + 1, high)

    def partition1(self, arr, low, high):
        pivot = arr[int((low + high) / 2)]
        i = low - 1
        j = high + 1

        while True:
            i += 1
            print(i)
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1

            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]

    def sort2(self, arr, low, high):
        if low < high:
            p = self.partition2(arr, low, high)
            self.sort2(arr, low, p - 1)
            self.sort2(arr, p + 1, high)

    def partition2(self, arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i
