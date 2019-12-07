# 직사각형에서 탈출
import sys


def square(x, y, w, h):
    lst = []
    length = w - x
    width = h - y
    lst.append(x)
    lst.append(y)
    lst.append(length)
    lst.append(width)
    return min(lst)  # 직사각형으로부터 거리에 따라 값이 달라지므로 최소값만을 출력


a, b, c, d = map(int, sys.stdin.readline().split())
print(square(a, b, c, d))
