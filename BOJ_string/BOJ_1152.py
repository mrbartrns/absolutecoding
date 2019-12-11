#  단어 입력 받고 단어의 갯수 세기
import sys


def solve(a):
    '''
    :param a: sentence
    :return: numbers of word
    '''
    a = list(a.split())
    b = len(a)
    return b


a = sys.stdin.readline()
b = solve(a)
print(b)
