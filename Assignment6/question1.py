from collections import deque
import heapq

# Goal state
GOAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

# Directions for moving the blank tile (up, down, left, right)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to find the position of the blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

# Function to generate possible next states
def generate_states(state):
    blank_i, blank_j = find_blank(state)
    next_states = []
    for move in MOVES:
        new_i, new_j = blank_i + move[0], blank_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [list(row) for row in state]
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            next_states.append(tuple(map(tuple, new_state)))
    return next_states

# DFS Algorithm
def dfs(initial_state):
    stack = [(initial_state, [])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == GOAL_STATE:
            return path
        if state not in visited:
            visited.add(state)
            for next_state in generate_states(state):
                stack.append((next_state, path + [next_state]))
    return None

# BFS Algorithm
def bfs(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == GOAL_STATE:
            return path
        if state not in visited:
            visited.add(state)
            for next_state in generate_states(state):
                queue.append((next_state, path + [next_state]))
    return None

# Heuristic function for A* (Manhattan distance)
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_i, goal_j = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# A* Search Algorithm
def a_star(initial_state):
    heap = [(manhattan_distance(initial_state), 0, initial_state, [])]
    visited = set()
    while heap:
        _, cost, state, path = heapq.heappop(heap)
        if state == GOAL_STATE:
            return path
        if state not in visited:
            visited.add(state)
            for next_state in generate_states(state):
                heapq.heappush(heap, (cost + 1 + manhattan_distance(next_state), cost + 1, next_state, path + [next_state]))
    return None

# Function to print the state
def print_state(state):
    for row in state:
        print(row)
    print()

if __name__ == "__main__":
    # Initial state
    initial_state = ((1, 2, 3), (5, 6, 0), (7, 8, 4))

                            
    '''
    # Solve using DFS                               # DFS cannot be used to solve this problem as it may run into 
    print("Solving using DFS:")                     # infinite loop causing stack overflow. (refer to screenshots)
    dfs_path = dfs(initial_state)
    if dfs_path:
        for state in dfs_path:
            print_state(state)
    else:
        print("No solution found using DFS.")
    '''

    # Solve using BFS
    print("Solving using BFS:")
    bfs_path = bfs(initial_state)
    if bfs_path:
        for state in bfs_path:
            print_state(state)
    else:
        print("No solution found using BFS.")

    # Solve using A*
    print("Solving using A*:")
    a_star_path = a_star(initial_state)
    if a_star_path:
        for state in a_star_path:
            print_state(state)
    else:
        print("No solution found using A*.")