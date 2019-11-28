#honey comb

import sys
"""
일반적인 등차 또는 등비수열이 아니므로, 수열의 일반항만 찾을 수 있다면 쉽게 구할 수 있다.
점화식을 사용하여 각 줄의 끝 숫자만 정리하면 해결이 간단하다.
'몇개의 방을 지나가는지'라는 것은, 즉 수열의 항을 찾으라는 뜻과 같다.
"""
def honey_comb(n):
    i = 0
    number = 0
    flag = True #while문을 멈추기 위한 상태 변화 저장
    if n == 1:
        return 1
    else:
        while flag:
            if 3 * (i - 1) * (i - 2) + 1 < n <= 3 * i * (i -1) + 1: #수열의 일반항
                number = i #만족 시 number에 i저장
                flag = False #break
            else:
                i += 1 #i에다 1씩 더하여 연산을 반복한다.
        return number

a = int(sys.stdin.readline())
print(honey_comb(a))