from typing import List

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(int_list: List[int]):
    min = int_list[0]
    sum = 0
    for n in int_list:
        if min >= n:
            min = n
        sum += n
    print(sum - min)

main()