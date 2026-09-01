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
    visited = []
    queue = []
    traverse_order = []
    queue.append(start)

    while queue:
        current = queue.pop(0)
        traverse_order.append(current)
        
        for s in tree[current]:
            if s is not visited:
                queue.append(s)
                visited.append(s)
    return traverse_order

        


print(BFS(tree,'A'))