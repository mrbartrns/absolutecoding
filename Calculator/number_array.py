import sys
import math

# Todo: 먼저 두개의 숫자를 받고 저장하는 것 구현하기
sign = ['+', '-', '*', '=']


class result:
    def __init__(self):
        self.result = [0]

    def save_result(self, number):
        self.result = [number]

    def print_result(self):
        return self.result[0]

    def __repr__(self):
        return str(self.result)


class PlusNum:
    def __init__(self, first, second):
        self.result = 0
        self.first = first
        self.second = second

    def add(self):
        add_result = self.first + self.second
        return add_result


def welcome():
    welcome_string = 'This is the Calculator for engineers.'
    print("\n" + "#" * len(welcome_string))
    print(f"{welcome_string}")
    print("#" * len(welcome_string) + "\n")
    print()


# Todo: 받는 숫자의 갯수에 상관 없이 계산 진행. 또한 숫자가 하나일 경우 저장된 결과와 연산해야 함.
def run_calculator():
    welcome()
    running = True
    number_save = result()  # 숫자를 받아서 결과값을 반환하는 객체
    # Todo: 저장된 값이 0일때 및 0이 아닐때를 구별하여, 0이 아닐 때에는 부호와 숫자만 입력받아도 계산이 가능하도록 할 것.
    while running:
        num1 = int(input("숫자를 입력하여 주십시오: "))
        input_sign = input("부호를 결정하여 주십시오: ")

        if input_sign == sign[0]:
            num2 = int(input("숫자를 입력하여 주십시오: "))
            plusnum = PlusNum(num1, num2)
            plusnum.add()
            number_save.save_result(plusnum.add())
            print(plusnum.add())

        elif input_sign == sign[3] or not input_sign:
            number_save.save_result(num1)
            print(number_save.print_result())

        yes_or_no = input('계속하시려면 yes를, 끝내시려면 no를 입력하여 주십시오: ')
        if yes_or_no == 'no':
            running = False
    print(number_save)


run_calculator()
