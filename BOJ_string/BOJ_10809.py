# 단어가 포함되어 있는 경우, 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1 출력.
import sys
a = sys.stdin.readline()
a.lower()
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    find_alpha = a.find(i) # 어떤 알파벳이 문자열 a 내부에 존재할 때:
    print(find_alpha, end=' ')
