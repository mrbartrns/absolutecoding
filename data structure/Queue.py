# 클래스를 이용하여 리스트로 큐 구현
"""
들어가야 할 메서드:
1. init : 빈 리스트 생성
2. dequeue: 리스트에서 요소를 끄집어냄. 빈 리스트일경우 -1을 반환
3 enqueue: 리스트에 요소를 추가.
4. 요소 출력
큐 자료구조는 선입선출법으로, 먼저 들어간 것을 먼저 나오게 해야 함.
"""
import sys
class Queue:
    # 리스트의 초기값
    def __init__(self):
        self.items = []

    # 큐에서 요소 끄집어내기
    def Dequeue(self):
        if len(self.items) == 0:  # 빈 배열일 때. if not self.items를 사용해도 무방
            return -1
        else:
            self.items.pop(0)
    #  큐에서 요소 추가, insert(0, n)을 사용해도 무방함
    def Enqueue(self, n):
        self.items.append(n)
        pass

    #  큐에서 첫번째 값을 보여줌.
    def peek(self):
        return self.items[0]


a = Queue()
for i in range(5):
    i += 1
    a.Enqueue(i)
a.Dequeue()
print(a.peek())