import random

# Constants for the dungeon generation
WIDTH = 20
HEIGHT = 10
CELLS = WIDTH * HEIGHT
ALIVE_THRESHOLD = 5
DEAD_THRESHOLD = 3

def initialize_grid(width, height):
    """Create a new grid with random walls."""
    return [[random.choice(['.', '#']) for _ in range(width)] for _ in range(height)]

def count_neighbors(grid, x, y):
    """Count the number of alive neighbors around a given cell."""
    count = 0
    for i in range(max(0, x-1), min(x+2, WIDTH)):
        for j in range(max(0, y-1), min(y+2, HEIGHT)):
            if grid[j][i] == '#':
                count += 1
    return count

def update_grid(grid):
    """Update the grid based on cellular automata rules."""
    new_grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = count_neighbors(grid, x, y)
            if grid[y][x] == '#':
                new_grid[y][x] = '#' if neighbors >= ALIVE_THRESHOLD else '.'
            else:
                new_grid[y][x] = '#' if neighbors >= DEAD_THRESHOLD else '.'
    return new_grid

def print_grid(grid):
    """Print the grid to the console."""
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    # Initialize a random dungeon
    dungeon = initialize_grid(WIDTH, HEIGHT)
    
    # Print the initial dungeon
    print("Initial Dungeon:")
    print_grid(dungeon)
    
    # Update the dungeon for 5 generations
    for _ in range(5):
        dungeon = update_grid(dungeon)
    
    # Print the updated dungeon
    print("\nUpdated Dungeon:")
    print_grid(dungeon)