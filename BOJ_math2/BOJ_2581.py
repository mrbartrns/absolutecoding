# 소수 구하기 2
import sys
import math


def prime_list(x, n):
    total = 0
    flag = [True] * (n + 1)
    m = int(math.sqrt(n))
    for i in range(2, m + 1):
        if flag[i]:
            for j in range(i + i, n + 1, i):
                flag[j] = False
    if x > 2:
        lst1 = [i for i in range(x, n + 1) if flag[i] == True]
    else:
        lst1 = [i for i in range(2, n + 1) if flag[i] == True]
    if not lst1:
        print(-1)
    else:
        for i in lst1:
            total += i
        print(total)
        print(min(lst1))


a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
prime_list(a, b)
