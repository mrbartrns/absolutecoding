import sys
import math
# Todo: 먼저 두개의 숫자를 받고 저장하는 것 구현하기


class result:
    def __init__(self):
        self.result = []

    def save_result(self, number):
        self.result = [number]

    def __repr__(self):
        return str(self.result)


class add_num:
    def __init__(self, first, second):
        self.result = 0
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result


def welcome():
    welcome_string = 'This is the Calculator for engineers.'
    print("\n" + "#" * len(welcome_string))
    print(f"{welcome_string}")
    print("#" * len(welcome_string) + "\n")


def run_calculator():
    welcome()
    running = True
    number_save = result()

    while running:
        num1 = int(sys.stdin.readline())
        num2 = int(sys.stdin.readline())
        sign = input("부호를 결정하여 주십시오: ")
        try:
            if sign == '+':
                addnum = add_num(num1, num2)
                addnum.add()
                number_save.save_result(addnum.add())
                print(addnum.add())
                yes_or_no = input('계속하시려면 yes를, 끝내시려면 no를 입력하여 주십시오: ')
                if yes_or_no == 'no':
                    running = False
        except:
            break
    print(number_save)


run_calculator()