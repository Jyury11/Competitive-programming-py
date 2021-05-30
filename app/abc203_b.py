from typing import List

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(int_list: List[int]):
    sum = 0
    for i in range(int_list[0]):
        for j in range(int_list[1]):
            sum = sum + ( (i + 1) * 100 + (j + 1))
    print(sum)


main()