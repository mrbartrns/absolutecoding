#  별 찍기
import sys
import math

def star(n):
    k = int(math.log(n, 3))
    if k == 0:
        print('*')
    else:
        print(n * '*')
        star(k - 1)
        print(n * '*')


star(3)