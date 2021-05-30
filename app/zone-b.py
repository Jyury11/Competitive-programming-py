from typing import List
import json

def main():
    int_list = [int(intl) for intl in input().split()]
    for i in range(int_list[0]):
        int_list2 = [int(intl) for intl in input().split()]
        print(makeLinearEquation(int_list[1], int_list[2], int_list2[0], int_list2[1]))


class func:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def __init__(self, x, y):
        self.x1 = x
        self.y1 = y

    def set(self, x, y):
        self.x2 = x
        self.y2 = y

    def ans(self, x, y):
        a1 = self.x1*


main()