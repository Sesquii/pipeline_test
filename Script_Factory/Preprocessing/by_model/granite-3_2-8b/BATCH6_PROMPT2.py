import sys
import random

def drunkards_walk(steps, size):
    """Generate a dungeon using the 'drunkard's walk' algorithm."""
    x, y = 0, 0
    grid = [['+' for _ in range(size)] for _ in range(size)]

    for _ in range(steps):
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1
        else: # right
            x += 1

        # Ensure the walker doesn't go out of bounds.
        x = max(0, min(size - 1, x))
        y = max(0, min(size - 1, y))

        grid[y][x] = ' '

    return grid

def print_grid(grid):
    """Print the generated dungeon grid."""
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH6_PROMPT2_{model_name}.py <steps> <size>")
        sys.exit(1)

    steps = int(sys.argv[1])
    size = int(sys.argv[2])

    dungeon = drunkards_walk(steps, size)
    print_grid(dungeon)