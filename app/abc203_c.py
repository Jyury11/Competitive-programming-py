from typing import List
from collections import Counter

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(int_list: List[int]):
    num = int_list[0]
    money = int_list[1]
    friend = Counter()
    for i in range(num):
        l = ([int(intl) for intl in input().split()])
        if l[0] <= money:
            money += l[1]
        else:
            friend[l[0]] += l[1]

    friend_sort = sorted(friend.items(), key=lambda x:x[0])
    for i in friend_sort:
        if i[0] <= money:
            money += i[1]
        else:
            print(money)
            return
    print(money)


main()