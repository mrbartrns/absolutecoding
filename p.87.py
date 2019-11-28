import sys

def solve(day, night, length):
    if length >= day > night:
        num = ((length - day) / (day - night)) + 1
        if num - int(num) != 0:
            return int(num) + 1
        else:
            return int(num)
    else:
        return -1

a, b, c = map(int,sys.stdin.readline().split())
print(solve(a, b, c))