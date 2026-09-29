from collections import deque

class GenericPuzzleGraph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}          # Adj list: node -> list of (neighbor_node, action)
        self.valid_states = set()

    def set_valid_states(self, valid_states_list):
        """Define which vertices are allowed in the graph."""
        self.valid_states = set(valid_states_list)

    def add_vertex(self, vertex):
        """Add a single vertex/state."""
        self.vertices.add(vertex)
        if vertex not in self.edges:
            self.edges[vertex] = []

    def add_edge(self, u, v, action="Transition"):
        """
        Add a directed edge u -> v with an action label.
        Only adds if both u and v are marked as valid states.
        """
        if u in self.valid_states and v in self.valid_states:
            self.add_vertex(u)
            self.add_vertex(v)
            self.edges[u].append((v, action))

    def bfs(self, start, target_condition_func):
        """Solves using Breadth-First Search (Guarantees shortest path)."""
        if start not in self.valid_states:
            return None, 0

        queue = deque([(start, [(start, "Start")])])
        visited = {start}
        nodes_explored = 0

        while queue:
            current, path = queue.popleft()
            nodes_explored += 1

            if target_condition_func(current):
                return path, nodes_explored

            for neighbor, action in self.edges.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [(neighbor, action)]))

        return None, nodes_explored

    def dfs(self, start, target_condition_func):
        """Solves using Depth-First Search."""
        if start not in self.valid_states:
            return None, 0

        stack = [(start, [(start, "Start")])]
        visited = set()
        nodes_explored = 0

        while stack:
            current, path = stack.pop()
            
            if current in visited:
                continue
            
            visited.add(current)
            nodes_explored += 1

            if target_condition_func(current):
                return path, nodes_explored

            for neighbor, action in self.edges.get(current, []):
                if neighbor not in visited:
                    stack.append((neighbor, path + [(neighbor, action)]))

        return None, nodes_explored


def build_water_jug_graph(cap_a, cap_b, invalid_states=None):
    """
    Example Builder: Generates the explicit graph (nodes and edges)
    for a 2-Jug problem, marking specified states as invalid.
    """
    if invalid_states is None:
        invalid_states = set()

    graph = GenericPuzzleGraph()

    # 1. Generate all possible nodes (vertices)
    all_nodes = [(a, b) for a in range(cap_a + 1) for b in range(cap_b + 1)]
    valid_nodes = [node for node in all_nodes if node not in invalid_states]
    
    graph.set_valid_states(valid_nodes)

    # 2. Build edges dynamically between valid vertices
    for a, b in valid_nodes:
        transitions = [
            ((cap_a, b), f"Fill Jug A ({cap_a}L)"),
            ((a, cap_b), f"Fill Jug B ({cap_b}L)"),
            ((0, b), "Empty Jug A"),
            ((a, 0), "Empty Jug B"),
        ]
        
        # Pour A -> B
        pour_a_to_b = min(a, cap_b - b)
        transitions.append(((a - pour_a_to_b, b + pour_a_to_b), "Pour Jug A -> Jug B"))

        # Pour B -> A
        pour_b_to_a = min(b, cap_a - a)
        transitions.append(((a + pour_b_to_a, b - pour_b_to_a), "Pour Jug B -> Jug A"))

        for next_state, action in transitions:
            graph.add_edge((a, b), next_state, action)

    return graph


# --- RUNTIME EXECUTION ---
if __name__ == "__main__":
    print("=== Generic State-Space Puzzle Solver ===")

    cap_a = int(input("Enter capacity of Jug A (e.g. 5): "))
    cap_b = int(input("Enter capacity of Jug B (e.g. 3): "))
    target = int(input("Enter target amount to measure (e.g. 4): "))

    # Optional: User-defined forbidden/invalid states
    invalid_input = input("Enter invalid states as comma-separated pairs like '1,1;2,2' (or press Enter for none): ")
    invalid_states = set()
    if invalid_input.strip():
        for pair in invalid_input.split(";"):
            a_val, b_val = map(int, pair.strip().split(","))
            invalid_states.add((a_val, b_val))

    # Build the state graph
    puzzle_graph = build_water_jug_graph(cap_a, cap_b, invalid_states)

    # Target condition: target volume is reached in either jug
    target_check = lambda state: state[0] == target or state[1] == target

    algo = input("Choose algorithm (1 for BFS, 2 for DFS): ").strip()
    
    start_state = (0, 0)
    if algo == "2":
        path, explored = puzzle_graph.dfs(start_state, target_check)
        algo_name = "DFS"
    else:
        path, explored = puzzle_graph.bfs(start_state, target_check)
        algo_name = "BFS"

    # Display results
    print(f"\n--- Results using {algo_name} ---")
    print(f"Total Nodes Explored: {explored}")
    
    if path:
        print(f"Solution Found in {len(path) - 1} steps:\n")
        print(f"{'Step':<6} | {'State':<15} | {'Action'}")
        print("-" * 45)
        for step, (state, action) in enumerate(path):
            print(f"{step:<6} | {str(state):<15} | {action}")
    else:
        print("No valid path exists to reach the target under given conditions/invalid states.")