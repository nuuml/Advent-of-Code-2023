import sys
sys.setrecursionlimit(10000000)

source = open('day8.txt', 'r').read().split("\n")


class Node:
    def __init__(self, val, l, r):
        self.val = val
        self.l = l
        self.r = r
        


def follow_steps(moves, nodes, curr, steps=0):
    for move in moves:
        win = 0
        newt = []
        for loc in curr:
            if loc[2] == 'Z':
                win += 1
            if move == 'L':
                newt.append(nodes[loc].l)
            else:
                newt.append(nodes[loc].r)
        if win == len(curr):
            return steps
        curr = newt
        print(curr)
        steps += 1
    return follow_steps(moves, nodes, curr, steps=steps)


instructions = source[0]
spots = {}

starts = []

for node in source[2::]:
    v = node.split(' = ')[0]
    l = node.split('(')[1].split(',')[0]
    r = node.split(', ')[1].split(')')[0]
    if v[2] == 'A':
        starts.append(v) 
    spots[v] = Node(v, l, r)
print(starts)
print(follow_steps(instructions, spots, starts))
