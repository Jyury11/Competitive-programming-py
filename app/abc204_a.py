from typing import List

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(int_list: List[int]):
    if int_list[0] == int_list[1]:
        print(int_list[0])
    else:
        print(3 - int_list[0] - int_list[1])

main()