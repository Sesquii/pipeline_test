# BATCH10_PROMPT6_{{model_name}}.py

import random
import time

class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[0 for _ in range(width)] for _ in range(height)]
        self.start = (1, 1)
        self.end = (height - 2, width - 2)

    def generate_maze(self):
        stack = [self.start]
        visited = set([self.start])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while stack:
            x, y = stack[-1]

            if len(visited) == self.width * self.height:
                break

            has_unvisited_neighbors = False
            for dx, dy in directions:
                nx, ny = x + 2 * dx, y + 2 * dy
                if (nx, ny) not in visited and 0 < nx < self.height - 1 and 0 < ny < self.width - 1:
                    has_unvisited_neighbors = True
                    break

            if has_unvisited_neighbors:
                for dx, dy in directions:
                    nx, ny = x + 2 * dx, y + 2 * dy
                    if (nx, ny) not in visited and 0 < nx < self.height - 1 and 0 < ny < self.width - 1:
                        self.maze[nx][ny] = 1
                        stack.append((nx, ny))
                        visited.add((nx, ny))
                        break
            else:
                stack.pop()

        self.maze[self.start[0]][self.start[1]] = 2
        self.maze[self.end[0]][self.end[1]] = 3

    def print_maze(self):
        for row in self.maze:
            print(''.join(['#' if cell == 0 else ' ' if cell == 1 else 'S' if cell == 2 else 'E' for cell in row]))

def main():
    width, height = 15, 15
    maze_generator = MazeGenerator(width, height)
    maze_generator.generate_maze()
    print("Initial Maze:")
    maze_generator.print_maze()

    while True:
        user_input = input("Enter your move (w/a/s/d) or 'q' to quit: ").lower()
        if user_input == 'q':
            break
        elif user_input not in ['w', 'a', 's', 'd']:
            print("Invalid move. Please use w, a, s, d.")
            continue

        x, y = maze_generator.start
        if user_input == 'w' and x > 1 and maze_generator.maze[x-1][y] != 0:
            x -= 2
        elif user_input == 'a' and y > 1 and maze_generator.maze[x][y-1] != 0:
            y -= 2
        elif user_input == 's' and x < height - 2 and maze_generator.maze[x+2][y] != 0:
            x += 2
        elif user_input == 'd' and y < width - 2 and maze_generator.maze[x][y+2] != 0:
            y += 2

        maze_generator.start = (x, y)

        if maze_generator.maze[x][y] == 3:
            print("Congratulations! You solved the maze!")
            break
        elif maze_generator.maze[x][y] == 0:
            print("You fell into a pit. Try again.")
            time.sleep(2)
            maze_generator.start = (1, 1)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
# BATCH10_PROMPT6_{{model_name}}.py

import random
import time
from typing import Tuple
import pytest

class MazeGenerator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.maze = [[0 for _ in range(width)] for _ in range(height)]
        self.start = (1, 1)
        self.end = (height - 2, width - 2)

    def generate_maze(self):
        stack = [self.start]
        visited = set([self.start])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while stack:
            x, y = stack[-1]

            if len(visited) == self.width * self.height:
                break

            has_unvisited_neighbors = False
            for dx, dy in directions:
                nx, ny = x + 2 * dx, y + 2 * dy
                if (nx, ny) not in visited and 0 < nx < self.height - 1 and 0 < ny < self.width - 1:
                    has_unvisited_neighbors = True
                    break

            if has_unvisited_neighbors:
                for dx, dy in directions:
                    nx, ny = x + 2 * dx, y + 2 * dy
                    if (nx, ny) not in visited and 0 < nx < self.height - 1 and 0 < ny < self.width - 1:
                        self.maze[nx][ny] = 1
                        stack.append((nx, ny))
                        visited.add((nx, ny))
                        break
            else:
                stack.pop()

        self.maze[self.start[0]][self.start[1]] = 2
        self.maze[self.end[0]][self.end[1]] = 3

    def print_maze(self):
        for row in self.maze:
            print(''.join(['#' if cell == 0 else ' ' if cell == 1 else 'S' if cell == 2 else 'E' for cell in row]))

def main():
    width, height = 15, 15
    maze_generator = MazeGenerator(width, height)
    maze_generator.generate_maze()
    print("Initial Maze:")
    maze_generator.print_maze()

    while True:
        user_input = input("Enter your move (w/a/s/d) or 'q' to quit: ").lower()
        if user_input == 'q':
            break
        elif user_input not in ['w', 'a', 's', 'd']:
            print("Invalid move. Please use w, a, s, d.")
            continue

        x, y = maze_generator.start
        if user_input == 'w' and x > 1 and maze_generator.maze[x-1][y] != 0:
            x -= 2
        elif user_input == 'a' and y > 1 and maze_generator.maze[x][y-1] != 0:
            y -= 2
        elif user_input == 's' and x < height - 2 and maze_generator.maze[x+2][y] != 0:
            x += 2
        elif user_input == 'd' and y < width - 2 and maze_generator.maze[x][y+2] != 0:
            y += 2

        maze_generator.start = (x, y)

        if maze_generator.maze[x][y] == 3:
            print("Congratulations! You solved the maze!")
            break
        elif maze_generator.maze[x][y] == 0:
            print("You fell into a pit. Try again.")
            time.sleep(2)
            maze_generator.start = (1, 1)

if __name__ == "__main__":
    main()

# Test suite for MazeGenerator class

@pytest.fixture
def maze_generator():
    return MazeGenerator(5, 5)

def test_generate_maze(maze_generator):
    maze_generator.generate_maze()
    assert maze_generator.maze[1][1] == 2
    assert maze_generator.maze[4][4] == 3
    for row in maze_generator.maze:
        assert sum(row) >= 2 and sum(row) <= 5

def test_print_maze(maze_generator):
    maze_generator.generate_maze()
    maze_generator.print_maze()  # This is a visual check, ensure the output matches expected

# Test suite for main function

@pytest.fixture
def maze_generator_main():
    return MazeGenerator(10, 10)

def test_main(maze_generator_main, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'w')
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 0

def test_main_invalid_move(maze_generator_main, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'x')
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 0

def test_main_solution_found(maze_generator_main, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 's' * (maze_generator_main.height - 3))
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 0

def test_main_fall_into_pit(maze_generator_main, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'w' * (maze_generator_main.height - 2))
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 0

def test_main_quit(maze_generator_main, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'q')
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 0
