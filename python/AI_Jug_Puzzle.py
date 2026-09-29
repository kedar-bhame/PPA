# Using 5l jug and 3l jug get 4 l
from collections import deque
def bfs_solver(initial_state, is_goal, get_neighbors):
    """Generic State-Space BFS Solver.
    Works for Jug Puzzles, River Crossing, 8-Puzzle, etc.   """
    queue = deque([(initial_state, [initial_state])])
    visited = {initial_state}
    while queue:
        current_state, path = queue.popleft()
        if is_goal(current_state):
            return path
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

CAPACITY_3 = 3
CAPACITY_5 = 5

def jug_is_goal(state):
    j3, j5 = state
    return j3 == 4 or j5 == 4


def jug_get_neighbors(state):
    j3, j5 = state
    neighbors = []

    # 1. Fill Jug 3
    neighbors.append((CAPACITY_3, j5))
    # 2. Fill Jug 5
    neighbors.append((j3, CAPACITY_5))
    # 3. Empty Jug 3
    neighbors.append((0, j5))
    # 4. Empty Jug 5
    neighbors.append((j3, 0))

    # 5. Pour Jug 3 -> Jug 5
    pour_3_to_5 = min(j3, CAPACITY_5 - j5)
    neighbors.append((j3 - pour_3_to_5, j5 + pour_3_to_5))
    # 6. Pour Jug 5 -> Jug 3
    pour_5_to_3 = min(j5, CAPACITY_3 - j3)
    neighbors.append((j3 + pour_5_to_3, j5 - pour_5_to_3))
    # Filter out duplicate transitions that don't alter state
    return [n for n in neighbors if n != state]
# Execute Solver
if __name__ == "__main__":
    start_state = (0, 0)
    solution = bfs_solver(start_state, jug_is_goal, jug_get_neighbors)
    if solution:
        print(f"Solution found in {len(solution) - 1} steps:\n")
        for step, state in enumerate(solution):
            print(f"Step {step}: 3L Jug = {state[0]}L, 5L Jug = {state[1]}L")
    else:
        print("No solution exists.")
