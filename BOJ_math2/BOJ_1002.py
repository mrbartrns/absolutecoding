# 터렛
# 원의 교접은 내접, 외접으로 나누어 생각해야 함. 시간복잡도가 O(1)
import sys
import math


def solve(x1, y1, r1, x2, y2, r2):
    length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    distance1 = r1 + r2
    distance2 = abs(r2 - r1)
    if x1 == x2 and y1 == y2 and r1 == r2:  # 두 원이 같은 원이기 때문에 접할 수 있는 위치는 무한대임.
        return -1
    else:
        if length < distance1:  # 두 점 사이의 거리가 두 반지름의 합보다 작은경우, 내접의 경우도 생각해야 함.
            if length == distance2:
                return 1
            elif length < distance2:
                return 0
            else:
                return 2
        elif length == distance1:
            return 1
        else:
            return 0


test = int(sys.stdin.readline())
for i in range(test):
    a, b, r1, c, d, r2 = map(int, sys.stdin.readline().split())
    print(solve(a, b, r1, c, d, r2))
