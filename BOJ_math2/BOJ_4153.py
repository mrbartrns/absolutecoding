#직각삼각형

import sys


def triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        lst1 = [a, b, c]
        lst1.sort()
        lst1.reverse()
        z = lst1[0]
        result = z ** 2 - (lst1[1] ** 2 + lst1[2] ** 2)
        if result == 0:
            return 1
        else:
            return -1
    else:
        return False


flag = True
while flag:
    a, b, c = map(int,sys.stdin.readline().split())
    solve = triangle(a, b, c)
    if solve == 1:
        print('right')
    elif solve == -1:
        print('wrong')
    if a == 0 and b == 0 and c == 0:
        flag = False
