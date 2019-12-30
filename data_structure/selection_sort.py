# difference between bubble sort and selection sort?
import sys


def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]


def selection_sort(arr):
    for i in range(len(arr)):
        minimumIndex = i
        minimumValue = arr[i]
        for j in range(i, len(arr)):
            if minimumValue >= arr[j]:
                minimumIndex = j
                minimumValue = arr[j]
        swap(arr, i, minimumIndex)
    return arr


arr = [3, 4, 5, 6, 1, 8, 9, 7, 2]
print(selection_sort(arr))