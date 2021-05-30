def main():
    arg = int(input())
    cnt = 0
    for i in range(arg):
        cnt += check_num(i + 1)
    print(cnt)

def check_num(num: int) -> int:
    if num % 2 == 0 or num - 1 < 3:
        return 0

    cnt = 0
    for i in range(3, num - 1):
        if num % i == 0:
            cnt += 1
    if cnt == 6:
        return 1
    else:
        return 0

main()