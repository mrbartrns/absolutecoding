# 피보나치 수열
import sys


def add(n):
    if n == 0:  # 알고리즘 및 재귀함수는 유한성을 만족해야 함. (종료 조건)
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return add(n - 1) + add(n - 2)


print(add(int(sys.stdin.readline())))