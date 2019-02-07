# class TimSort:
# def __init__(self):
#     self.RUN = 32

RUN = 32


# def insertionSort(self, arr, left, right):
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j >= left:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


# def mergeSort(self, arr, left, middle, right):
def mergeSort(arr, left, middle, right):
    len1, len2 = middle - left + 1, right - middle
    low, high = [], []
    for i in range(0, len1):
        low.append(arr[left + i])
    for i in range(0, len2):
        high.append(arr[middle + 1 + i])

    i, j, k = 0, 0, left

    while i < len1 and j < len2:

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

        while i < len1:
            arr[k] = low[i]
            k += 1
            i += 1

        while j < len2:
            arr[k] = high[j]
            k += 1
            j += 1


def timSort(arr, n):
    for i in range(0, n, RUN):
        insertionSort(arr, i, min((i + 31), (n - 1)))
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))

            mergeSort(arr, left, mid, right)

        size = 2 * size


# utility function to print the Array
def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
    print()

    # Driver program to test above function


if __name__ == "__main__":
    arr = [5, 21, 7, 23, 19]
    n = len(arr)
    print("Given Array is")
    printArray(arr, n)

    timSort(arr, n)

    print("After Sorting Array is")
    printArray(arr, n)
