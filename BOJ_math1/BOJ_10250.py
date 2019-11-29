#ACM 호텔
"""
지금 이 방법은 while문을 한 번 사용하는 시간복잡도가 O(n)인 프로그램이지만, 나머지와 몫을 이용한다면 O(1)로 해결이 가능하다.
(추가 예정)
"""
import sys

def hotel(h, w, n):
    if 1 <= h <= 99 and 1 <= w <= 99 and 1 <= n <= h * w:
        i = 0
        j = 1
        num = 0
        flag = True
        while flag:
            num += 1 #num이 n이 되면(사람의 순번) 자동으로 멈추고 room 번호를 출력하기 위함
            i += 1
            room = 100 * i + j #room 번호는 다음과 같이 쪼갤 수 있다.
            if num == n:
                flag = False
            elif i == h:
                j += 1 #j의 최대값인 w 값은 여기서 사용하지 않아도 가능하다. 위에 조건이 있기 때문
                i = 0
        return room
    else:
        return -1

test = int(sys.stdin.readline())
for i in range(test):
    a, b, c = map(int,sys.stdin.readline().split())
    print(hotel(a, b, c))