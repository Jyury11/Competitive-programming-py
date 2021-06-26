from typing import List

class StartBinaryNode:
    start = None
    end = None
    right = None
    left = None
    type = None
    left_num = 0

    def __init__(self, start, end, type):
        self.start = start
        self.end = end
        self.type = type
    def insert(self, next):
        if self.start < next.start:
            if self.right == None:
                self.right = next
            else:
                self.right.insert(next)
        else:
            self.left_num += 1
            if self.left == None:
                self.left = next
            else:
                self.left.insert(next)
    def search(self, node):
        cnt = 0
        if node.type == 1:
            if self.type == 1:
                if self.start <= node.end:
                    cnt += self.left_num
                    if self.end >= node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 2:
                if self.start <= node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 3:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end >= node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 4:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
        if node.type == 2:
            if self.type == 1:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end >= node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 2:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 3:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end >= node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 4:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
        if node.type == 3:
            if self.type == 1:
                if self.start <= node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 2:
                if self.start <= node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 3:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 4:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
        if node.type == 4:
            if self.type == 1:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 2:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 3:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
            if self.type == 4:
                if self.start < node.end:
                    cnt += self.left_num
                    if self.end > node.start:
                        cnt += 1
                    if self.right != None:
                        cnt += self.right.search(node)
        return cnt

def main():
    int_list = [int(intl) for intl in input().split()]
    check(int_list)

def check(n: List[int]):
    cnt = 0
    node_tree = None
    nodes = []
    for ij in range(n[0]):
        node_list = [int(intl) for intl in input().split()]
        start = node_list[1]
        end = node_list[2]
        type = node_list[0]
        node = StartBinaryNode(start, end, type)
        if ij == 0:
            node_tree = node
        else:
            node_tree.insert(node)
            cnt += node_tree.search(node)
        # nodes.append(node)
    # for node in nodes:
        # cnt += node_tree.search(node)
    print(cnt)
main()