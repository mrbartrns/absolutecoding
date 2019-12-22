# 순차탐색
import sys

def sequential_search1(arr, val):
    if len(arr) > 1:
        if arr[0] == val:
            print(val, 'True')
        else:
            sequential_search1(arr[1:], val)
    else:
        print(val, arr[0] == val)

def sequential_search2(arr, val):
    num = 0
    flag = True
    if len(arr) > 1:
        while flag:
            if arr[num] == val:
                print(val, 'True')
                flag = False
            else:
                num += 1


a = [2, 3, 6, 7, 10, 13]
sequential_search1(a, 13)