#아스키코드로 바꾸는 문제
import sys
"""
caution: 오직 한 글자만 입력이 가능함
"""
def ascii(c):
    c = c[0: len(c) -1] #enter의 입력을 지워주는 해결 방안
    asi = ord(c)

    return asi

a = sys.stdin.readline()
print(ascii(a))