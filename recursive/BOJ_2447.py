#  별 찍기
import sys
import math


class figure:
    def __init__(self, length, name):
        self.length = length
        self.name = name

    def get_area(self):
        area =  (math.sqrt(3) / 2)* self.length ** 2
        return area

    def get_name(self):
        return self.name

    def __del(self):
        print('object is deleted')
