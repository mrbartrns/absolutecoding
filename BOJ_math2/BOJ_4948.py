# 에네토스테리스의 채 응용, 베르트랑 공준
import sys


def prime_list(n):
    flag = [True] * (2 * n + 1)
    flag[1] = False
    x = int((2 * n) ** (1 / 2)) + 1
    for i in range(2, x):
        if flag[i]:
            for j in range(i + i, 2 * n + 1, i):
                flag[j] = False

    lst1 = [i for i in range(n + 1, 2 * n + 1) if flag[i] == True]
    return len(lst1)


chk = True
while chk:
    a = int(sys.stdin.readline())
    if a == 0:
        chk = False
    else:
        print(prime_list(a))
