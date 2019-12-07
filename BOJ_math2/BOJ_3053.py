#택시 기하학
import sys
import math


def solve(r): # R은 여기서 반지름임
    taxi = ((2 * r) ** 2) / 2
    euclid = math.pi * (r ** 2)
    print('%.6f' %euclid)
    print('%.6f' %taxi)

a = int(sys.stdin.readline())
solve(a)