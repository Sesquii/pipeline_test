import sys
import random

def generate_dungeon(width, height, steps):
    # Initialize map with walls
    dungeon = [['+' for _ in range(width)] for _ in range(height)]

    # Starting position (center of the map)
    x, y = width // 2, height // 2
    dungeon[y][x] = ' '  # Set starting position to floor

    # Drunkard's walk algorithm
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    for _ in range(steps):
        dx, dy = random.choice(directions)
        nx, ny = x + dx * 2, y + dy * 2

        if 0 <= nx < width and 0 <= ny < height:
            dungeon[ny][nx] = ' '
            dungeon[y + dy][x + dx] = ' '  # Carve out the wall between positions
            x, y = nx, ny

    return dungeon

def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(row))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python BATCH6_PROMPT2_<model_name>.py <width> <height> <steps>")
        sys.exit(1)

    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        steps = int(sys.argv[3])
    except ValueError:
        print("Width, height, and steps must be integers.")
        sys.exit(1)

    if width < 3 or height < 3:
        print("Width and height must be at least 3.")
        sys.exit(1)

    dungeon = generate_dungeon(width, height, steps)
    print_dungeon(dungeon)