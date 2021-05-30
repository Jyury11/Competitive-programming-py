from typing import List
from collections import Counter

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(int_list: List[int]):
    in_n = int_list[0]
    in_k = int_list[1]
    an = []
    for i in range(in_n):
        an.append([int(intl) for intl in input().split()])

    loop = in_n - in_k + 1
    min = -1
    for i in range(loop):
        for j in range(loop):
            center = []
            for k in range(in_k):
                for l in range(in_k):
                    center.append(an[(k) + (i)][(j) + (l)])

            center = sorted(center)

            index = (len(center) - 1) // 2
            if min == -1 or min > center[index]:
                    min = center[index]
    print(min)


main()