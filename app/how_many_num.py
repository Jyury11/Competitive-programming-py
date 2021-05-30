
while True:
    int_list = [int(intl) for intl in input().split()]
    if int_list[0] + int_list[1] == 0:
        break
    cnt = 0
    for i in range(1, int_list[0]):
        for j in range(i + 1, int_list[0]):
            ret = int_list[1] - i - j
            if ret <= 0:
                continue
            if j < ret <= int_list[0]:
                cnt += 1
                continue
    print(cnt)
