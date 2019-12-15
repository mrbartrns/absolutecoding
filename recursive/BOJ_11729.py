#  하노이의 탑
import sys


def func(n):
    if n == 1:
        print('*')
    else:
        func(n - 1)
        print('*' * n)
        func(n - 1)

#수정중
func(5)
#별찍기 연습중