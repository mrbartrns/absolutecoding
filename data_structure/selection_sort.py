# difference between bubble sort and selection sort?
import sys


def swap(arr, first, second):
    arr[first], arr[second] = arr[second], arr[first]

def selection_sort(arr, startIndex=0):
    for i in range(startIndex, len(arr)):
        minimumIndex = startIndex
        minimumValue = arr[startIndex]
        for j in range(startIndex, len(arr)):
            if minimumValue >= arr[j]:
                minimumIndex = i
                minimumValue = arr[i]
                swap(arr, startIndex, minimumIndex)
        startIndex += 1
    return arr

arr = [3, 4, 5, 6, 1, 8, 9, 7, 2]
print(selection_sort(arr))