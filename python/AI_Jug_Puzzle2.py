from collections import deque

class PureGraphPuzzleSolver:
    def __init__(self):
        self.vertices = set()
        self.edges = {}  # u -> list of (v, action_label)
        self.valid_states = set()

    def set_valid_states(self, valid_list):
        self.valid_states = set(valid_list)

    def add_edge(self, u, v, action="Transition"):
        """Adds directed edge u -> v only if both u and v are valid states."""
        if u in self.valid_states and v in self.valid_states:
            self.vertices.add(u)
            self.vertices.add(v)
            if u not in self.edges:
                self.edges[u] = []
            self.edges[u].append((v, action))

    def bfs(self, start, goal):
        """Finds shortest path using Breadth-First Search."""
        if start not in self.valid_states or goal not in self.valid_states:
            return None, 0

        queue = deque([(start, [(start, "Start State")])])
        visited = {start}
        nodes_explored = 0

        while queue:
            current, path = queue.popleft()
            nodes_explored += 1

            if current == goal:
                return path, nodes_explored

            for neighbor, action in self.edges.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [(neighbor, action)]))

        return None, nodes_explored

    def dfs(self, start, goal):
        """Finds path using Depth-First Search."""
        if start not in self.valid_states or goal not in self.valid_states:
            return None, 0

        stack = [(start, [(start, "Start State")])]
        visited = set()
        nodes_explored = 0

        while stack:
            current, path = stack.pop()

            if current in visited:
                continue

            visited.add(current)
            nodes_explored += 1

            if current == goal:
                return path, nodes_explored

            for neighbor, action in self.edges.get(current, []):
                if neighbor not in visited:
                    stack.append((neighbor, path + [(neighbor, action)]))

        return None, nodes_explored


def main():
    solver = PureGraphPuzzleSolver()

    print("=== Universal Graph Puzzle Solver ===")
    print("States can be strings or tuples (e.g., '0,0,0,0' or 'A')\n")

    # 1. Input Vertices
    v_count = int(input("Enter total number of vertices/states: "))
    all_vertices = []
    print(f"Enter {v_count} vertices (one per line):")
    for _ in range(v_count):
        all_vertices.append(input(" Vertex: ").strip())

    # 2. Input Invalid States
    invalid_input = input("\nEnter invalid/forbidden states separated by comma (or press Enter if none): ").strip()
    invalid_states = set([s.strip() for s in invalid_input.split(",") if s.strip()])
    
    valid_states = [v for v in all_vertices if v not in invalid_states]
    solver.set_valid_states(valid_states)

    # 3. Input Edges
    e_count = int(input("\nEnter total number of directed edges/transitions: "))
    print("Enter each edge as: Source, Destination, Action Description")
    print("Example: 0000, 1100, Farmer takes Goat")
    
    for i in range(e_count):
        edge_str = input(f" Edge {i+1}: ").strip()
        parts = [p.strip() for p in edge_str.split(",")]
        u = parts[0]
        v = parts[1]
        action = parts[2] if len(parts) > 2 else f"Move to {v}"
        solver.add_edge(u, v, action)

    # 4. Input Initial and Goal States
    print("\n--- Puzzle Objectives ---")
    start_state = input("Enter Initial State: ").strip()
    goal_state = input("Enter Goal State: ").strip()

    # 5. Algorithm Selection & Execution
    algo = input("Choose Algorithm (1 for BFS, 2 for DFS): ").strip()

    if algo == "2":
        path, explored = solver.dfs(start_state, goal_state)
        algo_name = "DFS"
    else:
        path, explored = solver.bfs(start_state, goal_state)
        algo_name = "BFS"

    # Display Output
    print(f"\n================ Results ({algo_name}) ================")
    print(f"Total Nodes Explored: {explored}")

    if path:
        print(f"Path Found in {len(path) - 1} steps:\n")
        print(f"{'Step':<6} | {'State':<20} | {'Action Taken'}")
        print("-" * 55)
        for idx, (state, action) in enumerate(path):
            print(f"{idx:<6} | {state:<20} | {action}")
    else:
        print("\nNo valid path exists from Initial State to Goal State under given valid transitions.")

if __name__ == "__main__":
    main()