#우주선문제
import sys
def minimum(x, y):
    n = 1
    flag = True
    length = y - x
    if y - x == 1:
        return 1
    else:
        while flag:
            n += 1
            if n % 2 == 0: #n이 짝수일때 아래식에 넣게 될경우, n을 변하게 하는 수 바로 다음 수에서 오류가 남
                if int(((n - 1) / 2) * ((n - 1) / 2 + 1)) + 1 < length <= int((n / 2) * (n / 2 + 1)):
                    flag = False
                    return n
            else:
                if int(((n - 1) / 2) * ((n - 1) / 2 + 1)) < length <= int((n / 2) * (n / 2 + 1)) + 1:
                    flag = False
                    return n

test = int(sys.stdin.readline())
for i in range(test):
    a , b = map(int, sys.stdin.readline().split())
    print(minimum(a, b))