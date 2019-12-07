#골드바흐의 추측
import sys
import math

def prime_list(n):
    lst2 = []
    if n % 2 != 0:
        return -1
    else:
        flag = [True] * n
        m = int(math.sqrt(n)) + 1
        for i in range(2, m):
            if flag[i]:
                for j in range(i+i, n, i):
                    flag[j] = False
        lst1 = [i for i in range(2, n) if flag[i] == True]
        sieve = [False] * n
        for a in lst1:
            b = n - a
            sieve[b] = True
            lst2 = [i for i in lst1 if sieve[i] == True]
        if len(lst2) % 2 != 0:
            idx = int(len(lst2)/ 2)
            print(lst2[idx], lst2[idx])
        else:
            print(lst2[int(len(lst2) / 2) - 1], lst2[int(len(lst2) / 2)])

test = int(sys.stdin.readline())
for i in range(test):
    prime_list(int(sys.stdin.readline()))