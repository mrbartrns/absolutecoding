#에네토스테리스의 채
"""
매우 중요하고 활용도가 높은 방법
일정 범위 또는 만족하는 숫자가 두개 이상일때 유용함
"""
import sys

def prime_list(m, n):
    x = int(n ** 1 / 2) + 1
    flag = [True] * (n + 1) #범위 내의 숫자를 모두 소수라고 가정
    flag[1] = False
    for i in range(2, x): #2, sqrt(n)까지의 숫자에 대하여
        if flag[i]:
            for j in range(i + i, n + 1, i):#i배수의 숫자들을 모두 False 처리함. i를 제외한 수부터
                flag[j] = False
    lst1 = [i for i in range(m, n + 1) if flag[i] == True]
    for i in lst1:
        print(i)

a, b = map(int,sys.stdin.readline().split())
prime_list(a, b)