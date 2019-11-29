#숫자의 합
import sys

def solve(a,b):
    '''
    :param a: int
    :param b: str
    :return: int
    '''
    sum = 0
    b = b[0:len(b) -1] #str입력시 엔터가 포함되므로 \n 제거 필요
    for i in range(a):
        c = int(b[i]) #문자열을 int로 바꿔주어 연산 필요
        sum += c #합을 저장

    return sum

a = int(sys.stdin.readline())
b = sys.stdin.readline()
print(solve(a,b))