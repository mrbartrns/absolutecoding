# binary search
import sys

def binary_search(lst, n):  # 리스트속의 n을 찾고 싶을 때:
    # 이진탐색은 리스트의 중간에서 부터 시작
    mid = int(len(lst) / 2)
    if len(lst) > 1:
        if lst[mid] < n:
            return binary_search(lst[mid:], n)  # 내가 찾고자 하는 수가 mid보다 작으면, lst의 범위를 mid이상으로 줄여서 다시 검색
        elif lst[mid] > n:
            return binary_search(lst[:mid], n)
        else:
            print(n, 'True')
    else:
        print(n, lst[0] == n)

# 재귀를 사용하지 않는다면?
def binary_search1(lst, n):
    mid = int(len(lst) / 2)
    if len(lst) > 1:
        if lst[mid] < n:
            