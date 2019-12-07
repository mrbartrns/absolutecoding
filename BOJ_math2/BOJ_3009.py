# 네번째 점
import sys


def sqare(x1, y1, x2, y2, x3, y3):
    flag = False
    x4 = 0
    y4 = 0
    lst1 = [x1, x2, x3]
    lst2 = [y1, y2, y3]
    for i in lst1:
        total1 = lst1.count(i)
        if total1 == 1:
            x4 = i
            break
    for j in lst2:
        total2 = lst2.count(j)
        if total2 == 1:
            y4 = j
            break
    print(x4, y4)

x1, y1 = map(int,sys.stdin.readline().split())
x2, y2 = map(int,sys.stdin.readline().split())
x3, y3 = map(int,sys.stdin.readline().split())
sqare(x1, y1, x2, y2, x3, y3)