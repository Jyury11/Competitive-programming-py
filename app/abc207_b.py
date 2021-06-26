from typing import List

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(n: List[int]):
    if n[0] == 0:
        print(0)
        return
    water = n[1]
    red = n[2] * n[3]
    if water >= red or red == 0:
        print(-1)
        return
    red_sum = 0
    water_sum = n[0]
    cnt = 0
    while(red_sum < water_sum):
        water_sum += water
        red_sum += red
        cnt += 1
    print(cnt)

main()