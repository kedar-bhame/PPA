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
#              2. All vertices & values (Key-Value Pairs)
#              3. Number of edges
#              4. All edges (Comma-separated in one line)
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
# 2. ENTER VERTICES AND VALUES AS KEY-VALUE PAIRS
# ==========================================================

print("\nEnter vertices and their string values in pairs.")
print("Example format: S0 value1, S2 value2 (commas are optional)")

# Replace commas with spaces so they don't count as extra tokens
raw_input_str = input("Enter all vertices and values in one line: ")
vertex_input = raw_input_str.replace(',', ' ').split()

if len(vertex_input) != n * 2:
    print("\nERROR!")
    print("Each vertex must have a corresponding value.")
    print("Expected tokens:", n * 2, "(", n, "pairs )")
    print("You entered:", len(vertex_input), "tokens.")
    exit()

vertex_dict = {}
for i in range(0, len(vertex_input), 2):
    v = vertex_input[i]
    val = vertex_input[i+1]
    vertex_dict[v] = val

vertices = list(vertex_dict.keys())


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
# 5. ENTER EDGES (Comma-separated in one line)
# ==========================================================

print("\n==================================================")
print("                    ENTER EDGES")
print("==================================================")

print("Enter all edges in one line separated by commas.")
print("Example format: A B, B C, C D")
print("The graph is UNDIRECTED (A B means A <-> B).\n")

edge_line = input("Enter all edges: ")

# Split by comma first to separate each edge pair
edge_pairs = [pair.strip() for pair in edge_line.split(",") if pair.strip()]

if len(edge_pairs) != e:
    print("\nERROR!")
    print(f"Expected {e} edges, but you entered {len(edge_pairs)} edges.")
    exit()

for pair in edge_pairs:
    edge = pair.split()
    
    if len(edge) != 2:
        print(f"ERROR: Invalid edge format '{pair}'. Use 'A B'.")
        exit()

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
# 9. DISPLAY VERTEX DICTIONARY (MAPPINGS)
# ==========================================================

print("\n==================================================")
print("             VERTEX KEY-VALUE MAPPINGS")
print("==================================================")

for v, val in vertex_dict.items():
    print(f"{v} -> {val}")


# ==========================================================
# 10. DISPLAY VALID STATES
# ==========================================================

print("\n==================================================")
print("                 VALID STATES")
print("==================================================")

print("Number of valid states:", len(valid_states))

for vertex in valid_states:

    print(f"{vertex}({vertex_dict[vertex]})", end=" ")

print()


# ==========================================================
# 11. DISPLAY INVALID STATES
# ==========================================================

print("\n==================================================")
print("                INVALID STATES")
print("==================================================")

print("Number of invalid states:", len(invalid_states))

for vertex in invalid_states:

    print(f"{vertex}({vertex_dict[vertex]})", end=" ")

print()


# ==========================================================
# 12. DISPLAY ORIGINAL GRAPH
# ==========================================================

print("\n==================================================")
print("                 ORIGINAL GRAPH")
print("==================================================")


for vertex in vertices:

    print(f"{vertex} ({vertex_dict[vertex]}) ->", end=" ")

    for neighbour in graph[vertex]:

        print(neighbour, end=" ")

    print()


# ==========================================================
# 13. CREATE VALID GRAPH
# ==========================================================

valid_graph = {}


for vertex in vertices:

    valid_graph[vertex] = []


for vertex in valid_states:

    for neighbour in graph[vertex]:

        if neighbour in valid_states:

            valid_graph[vertex].append(neighbour)


# ==========================================================
# 14. DISPLAY VALID / INVALID GRAPH
# ==========================================================

print("\n==================================================")
print("             GRAPH WITH STATES")
print("==================================================")


for vertex in vertices:

    if vertex in invalid_states:

        print(
            f"{vertex} ({vertex_dict[vertex]}) -> INVALID (X)"
        )

    else:

        print(
            f"{vertex} ({vertex_dict[vertex]}) -> VALID ->",
            end=" "
        )

        for neighbour in valid_graph[vertex]:

            print(neighbour, end=" ")

        print()


# ==========================================================
# 15. ENTER START AND GOAL
# ==========================================================

print("\n==================================================")
print("                 START AND GOAL")
print("==================================================")


start = input("Enter start vertex: ")

goal = input("Enter goal vertex: ")


# ==========================================================
# 16. CHECK START AND GOAL
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
# 17. DFS TRAVERSAL
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

    neighbours = valid_graph[current]


    for i in range(len(neighbours) - 1, -1, -1):

        neighbour = neighbours[i]


        if neighbour not in visited_dfs:

            stack.append(neighbour)


# ==========================================================
# 18. DISPLAY DFS TRAVERSAL
# ==========================================================

print("\n--------------------------------------------------")
print("              DFS TRAVERSAL ORDER")
print("--------------------------------------------------")


for i in range(len(visited_dfs)):

    v = visited_dfs[i]
    print(f"{v}({vertex_dict[v]})", end=" ")

print()


# ==========================================================
# 19. DFS ALL POSSIBLE PATHS
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
    path_formatted = [f"{v}({vertex_dict[v]})" for v in path]
    print(" -> ".join(path_formatted))


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

    v = visited_bfs[i]
    print(f"{v}({vertex_dict[v]})", end=" ")

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
    path_formatted = [f"{v}({vertex_dict[v]})" for v in path]
    print(" -> ".join(path_formatted))


# ==========================================================
# 23. FINAL COMPARISON
# ==========================================================

print("\n\n==================================================")
print("              DFS vs BFS COMPARISON")
print("==================================================")


print("\nDFS Traversal:")

for vertex in visited_dfs:

    print(f"{vertex}({vertex_dict[vertex]})", end=" -> ")

print("END")


print("\nBFS Traversal:")

for vertex in visited_bfs:

    print(f"{vertex}({vertex_dict[vertex]})", end=" -> ")

print("END")


print("\nNumber of DFS paths:", len(dfs_paths))

print("Number of BFS paths:", len(bfs_paths))


print("\n==================================================")
print("                 PROGRAM COMPLETE")
print("==================================================")