from typing import List

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(int_list: List[int]):
    for i in range(0,3):
        for j in range(i+1, 3):
            if int_list[i] == int_list[j]:
                print(int_list[3 - i - j])
                return
    print(0)


main()