tree = {
    'A':['B','C','D'],
    'B':['E'],
    'C':['x'],
    'D':['y'],
    'E':['z'],
    'x':[],
    'y':[],
    'z':[]
}

def BFS(tree,start):
    visited = [start]
    queue = [start]
    traversal_order = []

    while queue:
        current = queue.pop(0)
        traversal_order.append(current)

        for s in tree[current]:
            if s is not visited:
                queue.append(s)
                visited.append(s)
    return traversal_order                


print(BFS(tree,'A'))