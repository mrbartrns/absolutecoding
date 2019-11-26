#최소 경로
import sys

'''
SOLVE FUNCTION
'''
def solve(n):
    i = 0
    number = 0
    flag = True
    if n == 1:
        return 1
    else:
        while flag:
            if 3 * (i - 1) * (i - 2) + 1 < n <= 3 * i * (i - 1) + 1:
                number = i
                flag = False
            else:
                i += 1

    return number


num = int(sys.stdin.readline())
print(solve(num))