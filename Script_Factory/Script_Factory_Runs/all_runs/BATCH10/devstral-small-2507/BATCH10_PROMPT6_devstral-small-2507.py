# BATCH10_PROMPT6_{model_name}.py

import random
import time

class MazeGenerator:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.maze = [['#' for _ in range(width)] for _ in range(height)]
        self.visited = [[False for _ in range(width)] for _ in range(height)]
        self.complexity = 1

    def generate_maze(self):
        self._carve_passages_from(0, 0)
        return self.maze

    def _carve_passages_from(self, x, y):
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < self.width and 0 < ny < self.height and not self.visited[ny][nx]:
                self.visited[ny][nx] = True
                self.maze[y + dy//2][x + dx//2] = ' '
                self._carve_passages_from(nx, ny)

    def increase_complexity(self):
        self.complexity += 1
        if self.width < 30:
            self.width += 2
        if self.height < 30:
            self.height += 2
        # Add more walls or obstacles based on complexity
        for i in range(self.height):
            for j in range(self.width):
                if random.random() < 0.1 * self.complexity and self.maze[i][j] == ' ':
                    self.maze[i][j] = '#'

    def display_maze(self):
        for row in self.maze:
            print(''.join(row))

class MazeSolver:
    def __init__(self, maze, start=(0, 0), end=None):
        if end is None:
            end = (len(maze) - 1, len(maze[0]) - 1)
        self.maze = maze
        self.start = start
        self.end = end

    def solve(self):
        return self._solve_recursive(self.start[0], self.start[1])

    def _solve_recursive(self, x, y, visited=None):
        if visited is None:
            visited = set()

        if (x, y) == self.end:
            return True

        if not (0 <= x < len(self.maze)) or not (0 <= y < len(self.maze[0])):
            return False

        if (x, y) in visited or self.maze[x][y] == '#':
            return False

        visited.add((x, y))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            if self._solve_recursive(x + dx, y + dy, visited):
                return True

        return False

def main():
    maze_generator = MazeGenerator()
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        print(f"\nAttempt {attempts + 1}:")
        maze = maze_generator.generate_maze()
        maze_generator.increase_complexity()

        solver = MazeSolver(maze)
        start_time = time.time()

        if solver.solve():
            end_time = time.time()
            print("Maze solved successfully!")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            maze_generator.display_maze()
            break
        else:
            attempts += 1
            end_time = time.time()
            print(f"Failed to solve the maze. Time taken: {end_time - start_time:.2f} seconds")
            print("The maze will become more complex for the next attempt.")

    if attempts == max_attempts:
        print("\nMaximum attempts reached. You failed to solve the maze within the allowed attempts.")
    
if __name__ == "__main__":
    main()