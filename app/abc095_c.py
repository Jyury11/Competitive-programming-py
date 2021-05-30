from typing import List

def main():
    int_list = [int(intl) for intl in input().split()]
    print(check_prime(int_list))

def check_prime(args: List[int]) -> int:
    min = 0
    if args[0] + args[1] > args[2] * 2:
        if args[3] - args[4] > 0:
            if args[0] > args[2] * 2:
                min = args[4] * args[2] * 2 + (args[3] - args[4]) * args[2] * 2
            else:
                min = args[4] * args[2] * 2 + (args[3] - args[4]) * args[0]
        else:
            if args[1] > args[2] * 2:
                min = args[3] * args[2] * 2 + (args[4] - args[3]) * args[2] * 2
            else:
                min = args[3] * args[2] * 2 + (args[4] - args[3]) * args[1]
    else:
        min = args[0] * args[3] + args[1] * args[4]
    return min

main()