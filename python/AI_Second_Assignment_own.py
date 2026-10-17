n = int(input("Enter number of vertices: "))

print("Enter vertices and their string values in pairs.\n")
print("Example format: S0 value1 S1 value2 (commas are optional)\n")
raw_input_str = input("Enter all vertices and valuein one line : \n")
vertex_input = raw_input_str.replace(',', ' ').split()

if len(vertex_input) != n * 2 :
    print("Enter vertices count not match.\n")

vertex_dict = {}
for i in range(0,len(vertex_input),2):
    v = vertex_input[i]
    val = vertex_input[i+1]
    vertex_dict[v] = val
print(vertex_dict)

vertices = list(vertex_dict.keys())

e = int(input("Enter number of edges: "))
graph = {}

for vertex in vertices:
    graph[vertex] = []

print("Enter all edges in one line saperate by commas.\n")
print("Example format: S0 S1, S1 S2, S1 S3 \n")
print("The graph is UNDIRECTED (S0 S1 means S0 <-> S1).\n")

edge_line = input("Enter all edges : ")
edge_pairs = [pair.strip() for pair in edge_line.split(",")]

if len(edge_pairs) != e:
    print("Edge you enter are count not match")

for pair in edge_pairs:
    edge = pair.split()

    if len(edge) != 2:
        print(f"Error: Invalid edge format: {pair} please in key value pair")
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
    