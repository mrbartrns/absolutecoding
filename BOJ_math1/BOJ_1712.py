# 손익분기점 찾기(break_even_point)
"""
시간 제한이 0.35초 이므로, 시간복잡도가 O(n)이 아닌 O(1)이어야 함.
for문을 사용하면 시간 초과 발생
"""
import sys
# for문을 사용할 경우 O(n)
def break_even_point(a, b, c):
    n = 0
    flag = True
    if c > b:
        while flag:
            n += 1
            if n * (c - b) - a > 0:
                flag = False
    else:#c > b를 만족하지 못 할 경우 -1을 반환한다.
        return -1
    return n #판매대수 n값이 if문을 만족한다면, n을 반환한다.

# for문을 사용하지 않을 경우 O(1)
def break_even_point2(a, b, c):
    if c > b:
        n = a / (c - b)
        n += 1 #손익분기점은 그 점 이상일 때만 성립하므로, 1을 더함으로써 이를 만족시킨다.
    else:
        return -1 #손익분기점이 존재하지 않을 경우, -1을 반환한다.
    return int(n)

a, b, c = map(int,sys.stdin.readline().split())
print(break_even_point(a,b,c))