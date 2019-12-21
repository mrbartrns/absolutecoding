import sys
import matplotlib.pyplot as plt


def solve(lst):
    plt.plot(lst)  # (x축, y축, label = 순으로 생성됨. 하나의 변수만 존재할 경우 lst의 번수가 x축이 됨)

    plt.ylabel('some numbers')  # y축의 이름을 나타냄.

    return plt.show()


flag = True
lst = []
while flag:
    i = int(sys.stdin.readline())
    if i == -1:
        flag = False
    else:
        lst.append(i)

print(solve(lst))
