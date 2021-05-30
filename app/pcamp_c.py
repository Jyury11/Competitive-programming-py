from typing import List

def main():
    int_list = [int(intl) for intl in input().split()]
    m_point = []
    for i in range(int_list[0]):
        m_point.append([int(intl) for intl in input().split()])

    print(check_point(int_list, m_point))

def check_point(args: List[int], l: List[List[int]]) -> int:
    max = 0
    for i in range(args[1]):
        for j in range(i + 1, args[1]):
            max_tmp = 0
            for person in range(args[0]):
                if l[person][i] > l[person][j]:
                    max_tmp += l[person][i]
                else:
                    max_tmp += l[person][j]
            if max < max_tmp:
                max = max_tmp
    return max

main()