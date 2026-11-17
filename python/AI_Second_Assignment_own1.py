#-----------------------------------------
# steps:
#   1. Enter no. of vertives
#
#  
#------------------------------------------
 

#-----------------------------------------
#   1. Enter no. of vertives
#------------------------------------------
n = int(input("Enter number of vertices: "))

#-----------------------------------------
#   2. Enter vertices and their string values in pairs
#------------------------------------------
print("Enter vertices and their string values in pairs.\n")
print("Example format: S0 value1 S1 value2 (commas are optional)\n")
raw_input_str = input("Enter all vertices and values in one line : \n")
vertex_input = raw_input_str.replace(',', ' ').split()

if len(vertex_input) != n * 2 :
    print("Enter vertices and their count not match.\n")

vertex_dict = {}
for i in range(0,len(vertex_input),2):
    v = vertex_input[i]
    val = vertex_input[i+1]
    vertex_dict[v] = val
print(vertex_dict)

vertices = list(vertex_dict.keys())
print("vertices : ",vertices)

#-----------------------------------------
#   3. Enter no. of edeges
#------------------------------------------
e = int(input("Enter number of edges: "))

#-----------------------------------------
#   4. create Graph
#------------------------------------------
graph = {}

for vertex in vertices:
    graph[vertex] = []

#-----------------------------------------
#   5. Enter all edges comma saperated
#------------------------------------------
print("Enter all edges in one line saperate by commas.\n")
print("Example format: S0 S1, S1 S2, S1 S3 \n")
print("The graph is UNDIRECTED (S0 S1 means S0 <-> S1).\n")

edge_line = input("Enter all edges : ")
edge_pairs = [pair.strip() for pair in edge_line.split(",")]

if len(edge_pairs) != e:
    print("Edge you enter are count not match to number of edeges")
    exit()

for pair in edge_pairs:
    edge = pair.split()

    if len(edge) != 2:
        print(f"Error: Invalid edge format: {pair} please enter key value pair")
        exit()
    source = edge[0]
    destination = edge[1]

    if source not in vertices:
        print(f"Error: {source} not in vertix.")
        exit()

    if destination not in vertices:
        print(f"Error: {destination} not in vertix.")
        exit()

    graph[source].append(destination)
    graph[destination].append(source)

print(graph)

#-----------------------------------------
#   6. Enter valid states
#------------------------------------------    
valid_count = int(input(f"Enter how many valid states are there out of {n} states : "))
valid_input = input("Enter all valid state in one line : ").split()

if len(valid_input) != valid_count:
    print("\n Error!")
    print("no. of valid states enterd does not match  with valid state count.")
    exit()

valid_states = []

for vertex in valid_input:
    if vertex not in vertices:
        print("\n Error!")
        print(vertex, "does not exit")
        exit()
    valid_states.append(vertex)

#-----------------------------------------
#   7. Enter invalid states
#------------------------------------------
invalid_count = int(input(f"how many invalid states are there out of {n} states : "))
invalid_input = input("Enter all invalid states in one line : ").split()

if len(invalid_input) != invalid_count:
    print("\n Error")
    print("Number of invalid states enterd  does not match with invalid states count")
    exit()

invalid_states = []

for vertex in invalid_input:
    if vertex not in vertices:
        print("\n Error")
        print(vertex,"does not exit")
        exit()
    invalid_states.append(vertex)

#-----------------------------------------
#   8. check vertex are classified
#------------------------------------------
if ((len(valid_states) + len(invalid_states)) != n):
    print("\n Error!")
    print("Every vertex must be classified as valid or invalid")
    exit()

#-----------------------------------------
#   9. Display vertex dictionary
#------------------------------------------
for v,val in vertex_dict.items():
    print(f"{v} -> {val}")

#-----------------------------------------
#   10. Display valid states
#------------------------------------------

print("Number of valid states : ", len(valid_states))

for vertex in valid_states:
    print(f"{vertex}({vertex_dict[vertex]})", end=" ")
print()

#-----------------------------------------
#   11. Display invalid states
#------------------------------------------

print("Number of invalid states : ", len(invalid_states))

for vertex in invalid_states:
    print(f"{vertex}({vertex_dict[vertex]})", end=" ")
print()

#-----------------------------------------
#   12. Display original graph
#------------------------------------------
print("Original graph :")
for vertex in vertices:
    print(f"{vertex}({vertex_dict[vertex]}) ->", end=" ")

    for neighbour in graph[vertex]:
        print(neighbour, end=" ")
    print()

#-----------------------------------------
#   13. Create valid graph
#------------------------------------------
valid_graph = {}

for vertex in vertices:
    valid_graph[vertex] = []

for vertex in valid_states:
    for nei in graph[vertex]:
        if nei in valid_states:
            valid_graph[vertex].append(nei)

#-----------------------------------------
#   14. Display valid / invalid graph
#------------------------------------------

print("Graph with states : ")

for vertex in vertices :
    if vertex in invalid_states:
        print(f"{vertex}({vertex_dict[vertex]}) -> INVALID (X)")
    else :
        print(f"{vertex}({vertex_dict[vertex]}) -> VALID (X)",end=" ")

        for nei in valid_graph[vertex]:
            print(nei, end=" ")
        print()