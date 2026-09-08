graph = {
    'A':['B','C','D'],
    'B':['E'],
    'C':[],
    'D':[],
    'E':['F'],
    'F':[]
}

def BFS(graph,start):
    visited = [start]
    queue = [start]
    order = []
    while queue:
        current = queue.pop(0)
        order.append(current)
        for s in graph[current]:
            if s not in visited:
                queue.append(s)
                visited.append(s)
    return order

print(BFS(graph,'A'))

