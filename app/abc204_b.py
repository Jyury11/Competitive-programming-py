from typing import List

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(int_list: List[int]):
    sum = 0
    a_list = [int(intl) for intl in input().split()]
    for i in range(int_list[0]):
        if a_list[i] <= 10:
            continue
        else:
            sum += a_list[i] - 10
    print(sum)


main()