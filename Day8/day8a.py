source = open('day8.txt', 'r').read().split("\n")


class Node:
    def __init__(self, val, l, r):
        self.val = val
        self.l = l
        self.r = r
        
        
def follow_steps(moves, nodes, curr, steps=0):
    for move in moves:
        print(curr, steps)
        if curr == 'ZZZ':
            return steps
        steps += 1
        if move == 'L':
            curr = nodes[curr].l
        else:
            curr = nodes[curr].r
    return follow_steps(moves, nodes, curr, steps=steps)


instructions = source[0]
spots = {}


for node in source[2::]:
    v = node.split(' = ')[0]
    l = node.split('(')[1].split(',')[0]
    r = node.split(', ')[1].split(')')[0]
    spots[v] = Node(v, l, r)

print(follow_steps(instructions, spots, 'AAA'))
