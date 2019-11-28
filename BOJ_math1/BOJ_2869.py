#달팽이는 올라가고싶다.
"""
제한시간이 0.15초 이므로, while문으로 해결 시 시간초과에 유의 O(n), O(1)
"""

#틀린 풀이
def incorrect(day, night, length):
    if length >= day > night:
        n = length / (day - night) + 1 #아무 생각없이 실수 할 수 있는 부분. 그냥
        if n - int(n) != 0:
            n += 1
            return int(n)
        else:
            return int(n)
    else:
        return -1
"""
day에서 length에 도달하게 되면, break가 이루어져야 되는데 이 부분의 반영이 안되어있다.
"""
#바른 풀이 *풀이는 여러 방법이 존재함
def solve(day, night, length):
    if length >= day > night:
        n = (length - day) / (day - night) + 1
        if n - int(n) != 0:
            return int(n) + 1
        else:
            return int(n)
    else:
        return -1

#cf. while문으로 해결 할 경우
def solvewhile(day, length, night):
    n = 0
    sum = 0
    flag = True
    if length >= day > night:
        while flag:
            n += 1
            sum += day
            if sum >= length:
                return n
            else:
                sum -= night
        return n
    else:
        return -1