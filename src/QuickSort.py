array = [6, 4, 1, 8, 9, 2, 7, 5, 3]


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


def quick_sort(arr, low, high, message):
    print(message)
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p,"low")
        quick_sort(arr, p + 1, high,"high")
    return arr


print(array)
print(quick_sort(array, 0, array.__len__() - 1, "start"))
