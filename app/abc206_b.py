from typing import List

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(int_list: List[int]):
    n = int_list[0]
    i = 0
    cnt = 0
    while True:
        i += cnt
        if n <= i:
            print(cnt)
            return
        cnt += 1

main()