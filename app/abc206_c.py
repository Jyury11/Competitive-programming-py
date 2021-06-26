from typing import List

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(int_list: List[int]):
    n = int_list[0]
    arr = [int(intl) for intl in input().split()]
    ret = {}
    cnt = 0
    for i in range(n):
        if arr[i] in ret:
            ret[arr[i]].append(i)
        else:
            ret[arr[i]] = [i]
    for i in range(n):
        cnt += i
        cnt -= len(list(filter(lambda x: x > i, ret[arr[i]])))
    print(cnt)

main()