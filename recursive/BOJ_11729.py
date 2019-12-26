#  하노이의 탑
import sys


def hanoi(n, from_pos=1, to_pos=3, aux_pos=2):
    # n이 1일때, from과 to를 출력
    if n == 1:
        print(from_pos, to_pos)
    else:
        # n - 1개의 원판을 from에서 aux로 이동 시킴
        hanoi(n - 1, from_pos, aux_pos, to_pos)
        # 맨 아래의 원판을 from에서 to로 이동시킴
        print(from_pos, to_pos)
        # aux에 있는 n - 1 개의 원판을 to로 이동시킴
        hanoi(n - 1, aux_pos, to_pos, from_pos)


n = int(sys.stdin.readline())
total = 0
for i in range(n):
    total *= 2
    total += 1

print(total)
hanoi(n)