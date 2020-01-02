# insertion sort
import sys


def insertion_sort(arr):
    startIndex = 0
    minimumIndex = 0
    for i in range(startIndex):
        if arr[startIndex] > arr[i]:
            minimumIndex = i
            startIndex += 1
    return minimumIndex


arr = [3, 2, 1]
print(insertion_sort(arr))