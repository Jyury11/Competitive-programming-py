import queue

class Node:
    my = None
    nexts = []
    time = -1
    isCheck = False

    def __init__(self, num):
        self.my = num
        self.nexts = []
    def insert(self, next):
        self.nexts.append(next)
    def search(self, q):
        for i in self.nexts:
            if i.isCheck == False:
                i.time = self.time + 1
                i.isCheck = True
                q.put(i)

args = int(input())
nodes = []
for i in range(args):
    nodes.append(Node(i + 1))

for i in range(args):
    strl = input().split()
    int_list = [int(intl) for intl in strl]
    for j in range(int_list[1]):
        nodes[int_list[0] - 1].insert(nodes[int_list[2 + j] - 1])

q = queue.Queue()
nodes[0].isCheck = True
nodes[0].time = 0
nodes[0].search(q)

while not q.empty():
    next = q.get()
    next.search(q)

for i in nodes:
    print("%d %d" % (i.my, i.time))