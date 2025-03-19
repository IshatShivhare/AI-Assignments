import heapq

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

    def heuristic(self, node):
        x, y = node
        gx, gy = self.goal
        return abs(x - gx) + abs(y - gy)

    def best_first_search(self):
        open_list = []
        heapq.heappush(open_list, (self.heuristic(self.start), self.start, []))
        visited = set()

        while open_list:
            _, current, path = heapq.heappop(open_list)
            if current in visited:
                continue
            visited.add(current)

            if current == self.goal:
                print("Path found:", ''.join(path))
                return path

            x, y = current
            for direction, (dx, dy) in self.directions.items():
                nx, ny = x + dx, y + dy
                if self.is_valid(nx, ny) and (nx, ny) not in visited:
                    heapq.heappush(open_list, (self.heuristic((nx, ny)), (nx, ny), path + [direction]))

        print("No path found")
        return None

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

    def heuristic(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    x, y = divmod(state[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def best_first_search(self):
        open_list = []
        heapq.heappush(open_list, (self.heuristic(self.start), self.start, []))
        visited = set()

        while open_list:
            _, current, path = heapq.heappop(open_list)
            current_tuple = tuple(tuple(row) for row in current)
            if current_tuple in visited:
                continue
            visited.add(current_tuple)

            if current == self.goal:
                print("Path found:", ''.join(path))
                return path

            for direction in self.directions:
                new_state = self.move(current, direction)
                if new_state:
                    new_state_tuple = tuple(tuple(row) for row in new_state)
                    if new_state_tuple not in visited:
                        heapq.heappush(open_list, (self.heuristic(new_state), new_state, path + [direction]))

        print("No path found")
        return None

def main():
    while True:
        print("Choose an option:")
        print("1. Solve Maze")
        print("2. Solve 8-Puzzle")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # User input for Maze
            print("Enter the maze row by row (0 for open path, 1 for wall):")
            maze = []
            while True:
                row = input()
                if row.strip() == "":
                    break
                maze.append(list(map(int, row.split())))
            start = (0, 0)
            goal = (len(maze) - 1, len(maze[0]) - 1)
            maze_solver = Maze(maze, start, goal)
            maze_solver.best_first_search()
        elif choice == 2:
            # User input for 8-Puzzle
            print("Enter the start state for the 8-puzzle (3x3 grid, 0 for blank):")
            start_state = [list(map(int, input().split())) for _ in range(3)]
            print("Enter the goal state for the 8-puzzle (3x3 grid, 0 for blank):")
            goal_state = [list(map(int, input().split())) for _ in range(3)]
            puzzle_solver = EightPuzzle(start_state, goal_state)
            puzzle_solver.best_first_search()
        else:
            break
        
if __name__ == "__main__":
    main()
