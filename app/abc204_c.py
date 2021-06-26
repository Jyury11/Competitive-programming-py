from typing import List

class Node:
    my = None
    end = []

    def __init__(self, num):
        self.my = num
        self.end = []
        self.end.append(num)
    def insert(self, next):
        self.end.append(next.my)
        for e in next.end:
            if e != self.my:
                self.end.append(e)

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(int_list: List[int]):
    nodes = []
    for i in range(int_list[0]):
        nodes.append(Node(i + 1))
    for i in range(int_list[1]):
        m_list = [int(intl) for intl in input().split()]
        nodes[m_list[0] - 1].insert(nodes[m_list[1] - 1])
    sum = 0
    for node in nodes:
        for e in node.end:
            for e2 in nodes[e - 1].end:
                eflg = 0
                for e3 in node.end:
                    if e2 == e3:
                        eflg = 1
                if eflg == 0:
                    node.end.append(e2)
        sum += len(node.end)

    print(sum)

main()