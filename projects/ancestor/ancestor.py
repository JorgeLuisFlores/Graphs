
def earliest_ancestor(ancestors, starting_node):

    hash_table = {}
    solution = starting_node

    for i in range(len(ancestors)):
        if not ancestors[i][1] in hash_table:
            hash_table[ancestors[i][1]] = ancestors[i][0]

    while solution in hash_table:
        solution = hash_table[solution]

    if solution != starting_node:
        return solution
    else:
        return -1


def earliest_ancestor_fav_verbose(ancestors, starting_node):

    hash_table = {}
    iterating = True
    solution = starting_node

    print(solution)

    for i in range(len(ancestors)):
        if not ancestors[i][1] in hash_table:
            hash_table[ancestors[i][1]] = ancestors[i][0]
        print(hash_table)

    while iterating:
        if solution in hash_table:
            solution = hash_table[solution]
        else:
            iterating = False

    if solution != starting_node:
        return solution
    else:
        return -1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor_graph(ancestors, starting_node):

    s = Stack()
    earliest_list = [[starting_node]]
    neighbors = find_neighbors(starting_node, ancestors)

    if len(neighbors) == 0:
        return -1

    s.push(neighbors)
    earliest_list.append(neighbors)

    while s.size() > 0:
        curr = s.pop()
        for el in curr:
            next_node = find_neighbors(el, ancestors)
            if len(next_node) != 0:
                s.push(next_node)
                earliest_list.append(next_node)

    last = earliest_list[-1][0]

    return last


def find_neighbors(child, arr):
    neighbors = []
    for neighbor in arr:
        if neighbor[1] == child:
            neighbors.append(neighbor[0])
    return neighbors


earliest_ancestor = earliest_ancestor_graph
