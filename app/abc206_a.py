from typing import List

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(int_list: List[int]):
    n = int_list[0]
    m = int(n * 1.08)
    if m < 206:
        print("Yay!")
    if m == 206:
        print("so-so")
    if m > 206:
        print(":(")

main()