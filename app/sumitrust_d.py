class Node:
    my = 0
    next = []
    isComplete = False
    def __init__(self, num: int):
        self.my = num
    def search(self, num: int):
        if self.isComplete == True:
            return
        else:
            self.next[num % 10].isComplete = True
            if

def main():
    _ = int(input())
    S = input()
    print(check_num(S))

def check_num(num: str) -> int:
    first  = [False, False, False, False, False, False, False, False, False]
    second = [False, False, False, False, False, False, False, False, False]
    third  = [False, False, False, False, False, False, False, False, False]
    for i in range(len(num)):
        if first[i] == True:
            continue

        for j in range(i + 1, len(num)):
            if second[j] == True:
                continue
            for k in range(j + 1, len(num)):
                if third[k] == True:
                    continue
                if
    return len(d)

main()