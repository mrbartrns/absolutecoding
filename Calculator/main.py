import sys
import math



def welcome():
    welcome_string = 'This is the Calculator for engineers.'
    print("\n" + "#" * len(welcome_string))
    print(f"{welcome_string}")
    print("#" * len(welcome_string) + "\n")



sign = input("부호를 결정하여 주십시오: ")
print(sign)