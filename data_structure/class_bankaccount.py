# 계좌관리
"""
attribute:
계좌 초기 금액을 속성으로 하나 설정
생성자에서 초기 금액은 0으로 설정
속성은 private 으로 설정
method:
인출, 저축, 잔액 확인 세 가지 method 구현, 각각 현재 계좌 리턴
각 method도 private으로 설정
"""
import sys
class YourBankAccount:
    def __init__(self):
        self.BankAccount = 0

    def withdraw(self, n):
        if self.BankAccount - n < 0:
            return -1
        else:
            self.BankAccount -= n
            return self.BankAccount

    def saving(self, n):
        self.BankAccount += n
        return self.BankAccount

    def peek(self):
        print(self.BankAccount)


yourname = YourBankAccount()
yourname.saving(100000)
yourname.withdraw(3000)
yourname.peek()
