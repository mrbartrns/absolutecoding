# testing
import sys
import math

def prime_list1(lst):
    flag = False
    lst1 = []
    for i in lst:
        if i == 2:
            lst1.append(i)
        elif i > 2:
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                lst1.append(i)
                flag = False
    return len(lst1)

test = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
print(prime_list1(a))
