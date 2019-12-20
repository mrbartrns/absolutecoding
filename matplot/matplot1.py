import sys
import matplotlib.pyplot as plt


def solve(lst):
    plt.plot(lst)

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
