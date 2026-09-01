def bfs_using_list_queue(graph, start_node):
    visited = {start_node}
    queue = [start_node]  # Regular Python list as queue
    traversal_order = []

    while queue:
        current = queue.pop(0)  # Removes the first element (FIFO)
        traversal_order.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # Adds to the back

    return traversal_order

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs_using_list_queue(graph, 'A'))
# Output: ['A', 'B', 'C', 'D', 'E', 'F']