def main():
    arg = str(input().strip())
    check_len_actg(arg)

def check_len_actg(s: str):
    print(s.count('ZONe'))

main()