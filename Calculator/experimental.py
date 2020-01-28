import sys

'''
한줄에 부호까지 입력 받은 후 숫자와 부호를 따로 관리하여 저장하는 방법을 생각중.
'''

class add_num:

    def __init__(self):
        self.result = []
        self.total = 0

    def number_save(self, number):
        self.result.append(number)

    def number_sum(self):
        for i in range(len(self.result)):
            self.total += self.result[i]

    def __repr__(self):
        return str(self.total)


test = add_num()
sentense = input().split('+')
print(sentense)
for _ in sentense:
    _ = int(_)
    test.number_save(_)

test.number_sum()
print(test)
