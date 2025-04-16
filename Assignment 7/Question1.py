class Maze:
    def __init__(self, maze, start, goal):
        self.maze = maze
        self.start = start
        self.goal = goal
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] == 0

    def depth_limited_search(self, limit):
        def dls(node, depth):
            if node == self.goal:
                return True, []
            if depth == 0:
                return False, []
            x, y = node
            for direction, (dx, dy) in self.directions.items():
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny):
                    self.maze[x][y] = -1  # Mark as visited
                    found, path = dls((nx, ny), depth - 1)
                    self.maze[x][y] = 0  # Unmark
                    if found:
                        return True, [direction] + path
            return False, []

        found, path = dls(self.start, limit)
        if found:
            print("Path found:", ''.join(path))
        else:
            print("No path found within depth limit")

class EightPuzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def is_valid(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3

    def get_blank_position(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def move(self, state, direction):
        x, y = self.get_blank_position(state)
        dx, dy = self.directions[direction]
        nx, ny = x + dx, y + dy
        if self.is_valid(nx, ny):
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            return new_state
        return None

    def depth_limited_search(self, limit):
        def dls(state, depth):
            if state == self.goal:
                return True, []
            if depth == 0:
                return False, []
            for direction in self.directions:
                new_state = self.move(state, direction)
                if new_state:
                    found, path = dls(new_state, depth - 1)
                    if found:
                        return True, [direction] + path
            return False, []

        found, path = dls(self.start, limit)
        if found:
            print("Path found:", ''.join(path))
        else:
            print("No path found within depth limit")

def main():
    while True:
        print("Choose an option:")
        print("1. Solve Maze")
        print("2. Solve 8-Puzzle")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Enter the maze row by row (0 for open path, 1 for wall):")
            maze = []
            while True:
                row = input()
                if row.strip() == "":
                    break
                maze.append(list(map(int, row.split())))
            start = (0, 0)
            goal = (len(maze) - 1, len(maze[0]) - 1)
            limit = int(input("Enter the depth limit for the search: "))
            maze_solver = Maze(maze, start, goal)
            maze_solver.depth_limited_search(limit)

        elif choice == 2:
            print("Enter the start state for the 8-puzzle (3x3 grid, 0 for blank):")
            start_state = [list(map(int, input().split())) for _ in range(3)]
            print("Enter the goal state for the 8-puzzle (3x3 grid, 0 for blank):")
            goal_state = [list(map(int, input().split())) for _ in range(3)]
            limit = int(input("Enter the depth limit for the search: "))
            puzzle_solver = EightPuzzle(start_state, goal_state)
            puzzle_solver.depth_limited_search(limit)
        
        else:
            break

if __name__ == "__main__":
    main()
