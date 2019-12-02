# 문자열의 반복
import sys

def repeat_str(n, a):#글자 a를 n번 반복
    alist = list(a) #먼저 알파벳을 리스트로 바꿈. 근데 이렇게 할 필요 없음
    sum = ''
    for i in alist:
        i = i * n #cf. string에 대해서 i 보다는 c 기호를 더 많이 씀. c for character
        sum += i
    return sum

num = int(sys.stdin.readline())

for i in range(0, num):
    n, a = map(str, sys.stdin.readline().split())
    n = int(n)
    func = repeat_str(n, a)
    print(func)