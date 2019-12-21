# 스택은 큐보다 더 쉽다. (후입선출)

"""
스택 클래스에서 구현 되어야 할 요소들을 먼저 생각한다.
1. 초기 값
2. 비어있는지 확인하기
3. 요소 집어넣기
4. 요소 빼기
5. 사이즈 확인
6. 요소 찾기
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)  # 마지막 열에 요소 추가

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

class Queue:
    def __init__(self):
        self.items = []

    def Queue_empty(self):
        return self.items == []

    def Enqueue(self, item):
        self.items.append(item)

    def Dequeue(self):
        self.items.pop(0)

    def Queuesize(self):
        return len(self.items)

    def Queue_peek(self):
        return self.items[-1]

# 스택 클래스로 문자열 뒤집기

def reversestring(str):
    s = Stack()
    result = ""
    for i in str:
        s.push(i)
    while s.is_empty() != True:
        result += s.pop()  # string도 더할 수 있음.
    return result