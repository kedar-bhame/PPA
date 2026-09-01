from collections import deque

# Input graph structure
n = int(input("How Many Vertices? :"))
e = int(input("How Many Edges? : "))

adj_list = {}
print(adj_list)

print("Enter " + str(n) + " vertices")
for i in range(n):
    v = str(input("Enter Vertex :"))
    adj_list.setdefault(str(v), [])
print(adj_list)

print("Enter " + str(e) + " edges")
for i in range(e):
    v1 = str(input("Enter Starting Vertex:"))
    v2 = str(input("Enter Ending Vertex:"))
    adj_list[v1].append(v2)
print("Final Adjacency List:", adj_list)


# --- BFS IMPLEMENTATION ---
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    traversal_order = []

    while queue:
        current_node = queue.popleft()  # Remove from the front of the queue
        traversal_order.append(current_node)

        # Check all neighbors of the current node
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


# Driver code for BFS execution
start = input("Enter starting vertex for BFS: ")
if start in adj_list:
    result = bfs(adj_list, start)
    print("BFS Traversal Order:", " -> ".join(result))
else:
    print("Starting vertex not found in the graph!")