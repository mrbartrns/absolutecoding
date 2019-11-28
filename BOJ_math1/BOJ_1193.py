#분수찾기
"""
대각선으로 바라보았을 때, 짝수번째 항은 분자가 순차적으로 증가하고, 홀수번째 항은 분자가 순차적으로 감소
"""
import sys


def solve(num):
    flag = True #while문의 종료를 위한 상태 변경 변수
    n = 1
    if num == 1:
        return '%d/%d' % (1, 1)

    else:
        while flag: #이때 n은 분모 또는 분자가 된다.
            n += 1
            previous = (n * (n - 1)) / 2 # num은 등차수열의 합으로 이루어진 전 항과 후 항 사이에 존재한다.
            after = (n * (n + 1)) / 2
            if previous < num <= after:
                flag = False

        if n % 2 == 1:
            return '%d/%d' % ((after - num + 1), (num - previous))

        else:
            return '%d/%d' % ((num - previous), (after - num + 1))


a = int(sys.stdin.readline())
print(solve(a))