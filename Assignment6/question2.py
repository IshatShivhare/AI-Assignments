from collections import deque
import heapq

# Maze representation (0 = path, 1 = wall)
MAZE = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Directions for moving (up, down, left, right)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Start and goal positions
START = (0, 0)
GOAL = (4, 4)

# Function to check if a position is valid
def is_valid(x, y):
    return 0 <= x < len(MAZE) and 0 <= y < len(MAZE[0]) and MAZE[x][y] == 0

# DFS Algorithm
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (x, y), path = stack.pop()
        if (x, y) == goal:
            return path
        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    stack.append(((nx, ny), path + [(nx, ny)]))
    return None

# BFS Algorithm
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return None

# Heuristic function for A* (Manhattan distance)
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# A* Search Algorithm
def a_star(start, goal):
    heap = [(manhattan_distance(start[0], start[1], goal[0], goal[1]), 0, start, [start])]
    visited = set()
    while heap:
        _, cost, (x, y), path = heapq.heappop(heap)
        if (x, y) == goal:
            return path
        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in MOVES:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    heapq.heappush(heap, (cost + 1 + manhattan_distance(nx, ny, goal[0], goal[1]), cost + 1, (nx, ny), path + [(nx, ny)]))
    return None

# Function to print the maze with the path
def print_maze_with_path(path):
    maze_copy = [row[:] for row in MAZE]
    for (x, y) in path:
        maze_copy[x][y] = 2  # Mark the path
    for row in maze_copy:
        print(" ".join(str(cell) for cell in row))
    print()

if __name__ == "__main__":
    # Solve using DFS
    print("Solving using DFS:")
    dfs_path = dfs(START, GOAL)
    if dfs_path:
        print_maze_with_path(dfs_path)
    else:
        print("No solution found using DFS.")

    # Solve using BFS
    print("Solving using BFS:")
    bfs_path = bfs(START, GOAL)
    if bfs_path:
        print_maze_with_path(bfs_path)
    else:
        print("No solution found using BFS.")

    # Solve using A*
    print("Solving using A*:")
    a_star_path = a_star(START, GOAL)
    if a_star_path:
        print_maze_with_path(a_star_path)
    else:
        print("No solution found using A*.")