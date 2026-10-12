# ==========================================================
#              DFS + BFS GRAPH PROGRAM
#              FARMER-WOLF-GOAT-CABBAGE
#
#              NO LIBRARIES
#
#              DFS -> STACK
#              BFS -> QUEUE
#
#              USER ENTERS:
#              1. Number of vertices
#              2. All vertices
#              3. Number of edges
#              4. All edges
#              5. Valid states
#              6. Invalid states
#              7. Start vertex
#              8. Goal vertex
# ==========================================================


# ==========================================================
# 1. ENTER NUMBER OF VERTICES
# ==========================================================

print("==================================================")
print("             DFS AND BFS GRAPH")
print("==================================================")

n = int(input("\nEnter number of vertices: "))


# ==========================================================
# 2. ENTER ALL VERTICES IN ONE LINE
# ==========================================================

vertices = input("\nEnter all vertices in one line: ").split()


if len(vertices) != n:

    print("\nERROR!")
    print("You entered", len(vertices), "vertices.")
    print("Expected:", n)

    exit()


# ==========================================================
# 3. ENTER NUMBER OF EDGES
# ==========================================================

e = int(input("\nEnter number of edges: "))


# ==========================================================
# 4. CREATE GRAPH
# ==========================================================

graph = {}

for vertex in vertices:

    graph[vertex] = []


# ==========================================================
# 5. ENTER EDGES
# ==========================================================

print("\n==================================================")
print("                    ENTER EDGES")
print("==================================================")

print("Enter each edge in the form:")
print("A B")
print()
print("The graph is UNDIRECTED.")
print("Therefore A B means A <-> B.")


for i in range(e):

    print("\nEdge", i + 1, ":", end=" ")

    edge = input().split()

    source = edge[0]
    destination = edge[1]


    if source not in vertices:

        print("ERROR:", source, "is not a vertex.")
        exit()


    if destination not in vertices:

        print("ERROR:", destination, "is not a vertex.")
        exit()


    # Store edges in the SAME ORDER
    # in which the user entered them.

    graph[source].append(destination)
    graph[destination].append(source)


# ==========================================================
# 6. ENTER VALID STATES
# ==========================================================

print("\n==================================================")
print("                 VALID STATES")
print("==================================================")


valid_count = int(
    input("How many valid states are there: ")
)


valid_input = input(
    "Enter all valid states in one line: "
).split()


if len(valid_input) != valid_count:

    print("\nERROR!")
    print("Number of valid states entered does not match.")

    exit()


valid_states = []


for vertex in valid_input:

    if vertex not in vertices:

        print("ERROR:", vertex, "does not exist.")

        exit()

    valid_states.append(vertex)


# ==========================================================
# 7. ENTER INVALID STATES
# ==========================================================

print("\n==================================================")
print("                INVALID STATES")
print("==================================================")


invalid_count = int(
    input("How many invalid states are there: ")
)


invalid_input = input(
    "Enter all invalid states in one line: "
).split()


if len(invalid_input) != invalid_count:

    print("\nERROR!")
    print("Number of invalid states entered does not match.")

    exit()


invalid_states = []


for vertex in invalid_input:

    if vertex not in vertices:

        print("ERROR:", vertex, "does not exist.")

        exit()

    invalid_states.append(vertex)


# ==========================================================
# 8. CHECK WHETHER ALL VERTICES ARE CLASSIFIED
# ==========================================================

if len(valid_states) + len(invalid_states) != n:

    print("\nERROR!")
    print("Every vertex must be classified as either")
    print("VALID or INVALID.")

    exit()


# ==========================================================
# 9. DISPLAY VALID STATES
# ==========================================================

print("\n==================================================")
print("                 VALID STATES")
print("==================================================")

print("Number of valid states:", len(valid_states))

for vertex in valid_states:

    print(vertex, end=" ")

print()


# ==========================================================
# 10. DISPLAY INVALID STATES
# ==========================================================

print("\n==================================================")
print("                INVALID STATES")
print("==================================================")

print("Number of invalid states:", len(invalid_states))

for vertex in invalid_states:

    print(vertex, end=" ")

print()


# ==========================================================
# 11. DISPLAY ORIGINAL GRAPH
# ==========================================================

print("\n==================================================")
print("                 ORIGINAL GRAPH")
print("==================================================")


for vertex in vertices:

    print(vertex, "->", end=" ")

    for neighbour in graph[vertex]:

        print(neighbour, end=" ")

    print()


# ==========================================================
# 12. CREATE VALID GRAPH
# ==========================================================

valid_graph = {}


for vertex in vertices:

    valid_graph[vertex] = []


for vertex in valid_states:

    for neighbour in graph[vertex]:

        if neighbour in valid_states:

            valid_graph[vertex].append(neighbour)


# ==========================================================
# 13. DISPLAY VALID / INVALID GRAPH
# ==========================================================

print("\n==================================================")
print("             GRAPH WITH STATES")
print("==================================================")


for vertex in vertices:

    if vertex in invalid_states:

        print(
            vertex,
            "-> INVALID (X)"
        )

    else:

        print(
            vertex,
            "-> VALID ->",
            end=" "
        )

        for neighbour in valid_graph[vertex]:

            print(neighbour, end=" ")

        print()


# ==========================================================
# 14. ENTER START AND GOAL
# ==========================================================

print("\n==================================================")
print("                 START AND GOAL")
print("==================================================")


start = input("Enter start vertex: ")

goal = input("Enter goal vertex: ")


# ==========================================================
# 15. CHECK START AND GOAL
# ==========================================================

if start not in vertices:

    print("ERROR: Start vertex does not exist.")

    exit()


if goal not in vertices:

    print("ERROR: Goal vertex does not exist.")

    exit()


if start in invalid_states:

    print("ERROR: Start vertex is INVALID.")

    exit()


if goal in invalid_states:

    print("ERROR: Goal vertex is INVALID.")

    exit()


# ==========================================================
# ==========================================================
#                       DFS
# ==========================================================
# ==========================================================


print("\n\n==================================================")
print("                    DFS")
print("==================================================")


print("\nDFS uses STACK")
print("STACK = LIFO")
print("Last In -> First Out")


# ==========================================================
# 16. DFS TRAVERSAL
# ==========================================================

stack = []

visited_dfs = []


# Put starting vertex into stack

stack.append(start)


while len(stack) > 0:

    # Remove the LAST vertex
    # because stack follows LIFO.

    current = stack.pop()


    # Ignore already visited vertices

    if current in visited_dfs:

        continue


    # Visit current vertex

    visited_dfs.append(current)


    # ------------------------------------------------------
    # Add neighbours to STACK
    # ------------------------------------------------------
    #
    # We add them in reverse order.
    #
    # Example:
    #
    # A -> B C D
    #
    # Stack receives:
    #
    # D
    # C
    # B
    #
    # B is therefore processed first.
    #
    # ------------------------------------------------------

    neighbours = valid_graph[current]


    for i in range(len(neighbours) - 1, -1, -1):

        neighbour = neighbours[i]


        if neighbour not in visited_dfs:

            stack.append(neighbour)


# ==========================================================
# 17. DISPLAY DFS TRAVERSAL
# ==========================================================

print("\n--------------------------------------------------")
print("              DFS TRAVERSAL ORDER")
print("--------------------------------------------------")


for i in range(len(visited_dfs)):

    print(visited_dfs[i], end=" ")

print()


# ==========================================================
# 18. DFS ALL POSSIBLE PATHS
# ==========================================================

print("\n--------------------------------------------------")
print("             ALL DFS PATHS")
print("--------------------------------------------------")


dfs_stack = []

dfs_paths = []


# The STACK stores complete paths

dfs_stack.append([start])


while len(dfs_stack) > 0:

    # Remove the LAST path

    current_path = dfs_stack.pop()


    current_vertex = current_path[-1]


    # ------------------------------------------------------
    # If goal is reached
    # ------------------------------------------------------

    if current_vertex == goal:

        dfs_paths.append(current_path)

        continue


    # ------------------------------------------------------
    # Explore every possible neighbour
    # ------------------------------------------------------

    neighbours = valid_graph[current_vertex]


    # Reverse order for STACK

    for i in range(len(neighbours) - 1, -1, -1):

        neighbour = neighbours[i]


        # Prevent cycle

        if neighbour not in current_path:

            new_path = current_path.copy()

            new_path.append(neighbour)

            dfs_stack.append(new_path)


# PRINT ALL DFS PATHS HERE
for path in dfs_paths:
    print(" -> ".join(path))


# ==========================================================
# 
# ==========================================================
# ==========================================================
#                       BFS
# ==========================================================
# ==========================================================


print("\n\n==================================================")
print("                    BFS")
print("==================================================")


print("\nBFS uses QUEUE")
print("QUEUE = FIFO")
print("First In -> First Out")


# ==========================================================
# 20. BFS TRAVERSAL
# ==========================================================

queue = []

visited_bfs = []


# Put starting vertex into queue

queue.append(start)


while len(queue) > 0:

    # Remove FIRST vertex
    # because queue follows FIFO.

    current = queue.pop(0)


    # Ignore already visited vertices

    if current in visited_bfs:

        continue


    # Visit current vertex

    visited_bfs.append(current)


    # ------------------------------------------------------
    # Add neighbours to BACK of queue
    # ------------------------------------------------------

    for neighbour in valid_graph[current]:

        if neighbour not in visited_bfs:

            queue.append(neighbour)


# ==========================================================
# 21. DISPLAY BFS TRAVERSAL
# ==========================================================

print("\n--------------------------------------------------")
print("              BFS TRAVERSAL ORDER")
print("--------------------------------------------------")


for i in range(len(visited_bfs)):

    print(visited_bfs[i], end=" ")

print()


# ==========================================================
# 22. BFS ALL POSSIBLE PATHS
# ==========================================================

print("\n--------------------------------------------------")
print("             ALL BFS PATHS")
print("--------------------------------------------------")


bfs_queue = []

bfs_paths = []


# The QUEUE stores complete paths

bfs_queue.append([start])


while len(bfs_queue) > 0:

    # Remove FIRST path

    current_path = bfs_queue.pop(0)


    current_vertex = current_path[-1]


    # ------------------------------------------------------
    # If goal is reached
    # ------------------------------------------------------

    if current_vertex == goal:

        bfs_paths.append(current_path)

        continue


    # ------------------------------------------------------
    # Explore every neighbour
    # ------------------------------------------------------

    for neighbour in valid_graph[current_vertex]:


        # Prevent cycle

        if neighbour not in current_path:

            new_path = current_path.copy()

            new_path.append(neighbour)


            # Add new path to BACK of queue

            bfs_queue.append(new_path)


# PRINT ALL BFS PATHS HERE
for path in bfs_paths:
    print(" -> ".join(path))


# ==========================================================
# 24. FINAL COMPARISON
# ==========================================================

print("\n\n==================================================")
print("              DFS vs BFS COMPARISON")
print("==================================================")


print("\nDFS Traversal:")

for vertex in visited_dfs:

    print(vertex, end=" -> ")

print("END")


print("\nBFS Traversal:")

for vertex in visited_bfs:

    print(vertex, end=" -> ")

print("END")


print("\nNumber of DFS paths:", len(dfs_paths))

print("Number of BFS paths:", len(bfs_paths))


print("\n==================================================")
print("                 PROGRAM COMPLETE")
print("==================================================")