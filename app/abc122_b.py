def main():
    arg = str(input().strip())
    print(check_len_actg(arg))

def check_len_actg(s: str) -> int:
    max_len = 0
    itr_len = 0
    for i in s:
        if i == 'A' or i == 'C' or i == 'T' or i == 'G':
            itr_len += 1
        else:
            if max_len < itr_len:
                max_len = itr_len
            itr_len = 0
    if max_len < itr_len:
        return itr_len
    return max_len

main()