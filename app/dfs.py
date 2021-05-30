class Node:
    my = None
    nexts = []
    first = 0
    end = 0

    def __init__(self, num):
        self.my = num
        self.nexts = []
    def insert(self, next):
        self.nexts.append(next)
    def search(self, time, nodes):
        if self.first != 0 or self.end != 0:
            return time
        if self.first == 0:
            self.first = time
            time += 1
        for i in self.nexts:
            for j in nodes:
                if j.my == i and self.my != j.my:
                    time = j.search(time, nodes)
                    break
        if self.end == 0:
            self.end = time
            time += 1
        return time

args = int(input())
nodes = []
for i in range(args):
    strl = input().split()
    int_list = [int(intl) for intl in strl]
    n = Node(int_list[0])
    for j in range(int_list[1]):
        n.insert(int_list[2 + j])
    nodes.append(n)
time = 1

for i in nodes:
    time = i.search(time, nodes)

for i in nodes:
    print("%d %d %d" % (i.my, i.first, i.end))