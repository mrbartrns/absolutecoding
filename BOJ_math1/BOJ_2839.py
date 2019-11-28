# 가장 작은 합 찾기
import sys
"""
만족하는 수가 하나 이상일 경우, [False] 리스트 인덱스에 값을 저장하면 편리하다
"""

def sugar(n):
    flag = [False] * n  # a를 만족하는 수가 하나가 아니기 때문에 False로 이루어진 list를 만들어 저장함.
    a = 0
    for a in range(0, n):
        r = n - (5 * a)
        if r >= 0 and r % 3 == 0:
            flag[a] = True
        lst = [a for a in range(0, n) if flag[a] == True] #flag[a]가 True를 만족하는 a를 리스트로 만들어 출력

    if lst != []: #빈 리스트면 for를 만족하는 수가 없음
        lst.reverse() #lst중에서 가장 큰 수를 출력하기 위하여 찾아냄
        num1 = lst[0]
        num2 = (n - (5 * num1)) // 3
        return num1 + num2
    else:
        return -1


a = int(sys.stdin.readline())
print(sugar(a))
