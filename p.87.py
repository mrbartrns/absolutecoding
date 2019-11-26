import sys


def solve(word):
    word = word[0:len(word) - 1]
    flag = [False] * 30
    saved = -1
    for c in word:
        index = ord(c) - ord('a')
        if flag[index]:
            return False
        elif saved != -1 and saved != index:
            flag[saved] = True
        else:
            saved = index

    return True


n = int(sys.stdin.readline())
ans = 0
for i in range(0, n):
    if solve(sys.stdin.readline()):
        ans += 1

print(ans)