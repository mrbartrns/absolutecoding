#문자의 갯수를 대문자로 출력하기.
import sys

def solve(a):
    '''
    :param a: alphabet
    :return: ALPHABET
    '''
    a = a.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = list(str(a))
    max = -1
    lst = []
    idx = 0
    flag = False

    for i in alphabet:
        num = a.count(i)
        lst.append(num)

    for i in range(0, len(lst)):
        if max == lst[i] and flag == False:
            flag = True

        elif max < lst[i]:
            max = lst[i]
            idx = i
            flag = False

    if flag:
        return -1
    else:
        return alphabet[idx]


word = sys.stdin.readline()
a = solve(word)
if a == -1:
    print('?')
else:
    print(a)