import random
from typing import List, Tuple

def generate_dungeon(width: int = 50, height: int = 30) -> List[List[str]]:
    """Generate a dungeon using a 'growing tree' algorithm."""

    def carve_corridor(x1: int, y1: int, x2: int, y2: int) -> None:
        """Carve a corridor between two points."""
        length = min(abs(y2 - y1), abs(x2 - x1)) + 1

        for i in range(length):
            new_x = x1 + (x2 - x1) * i // length
            new_y = y1 + (y2 - y1) * i // length

            # Ensure we don't go out of bounds and there's no wall.
            if 0 <= new_x < width and 0 <= new_y < height:
                grid[new_y][new_x] = '.'

    def place_rooms() -> None:
        """Place random rooms inside the dungeon."""
        for _ in range(10):  # Adjust room count as needed
            x, y = random.randint(0, width - 2), random.randint(0, height - 2)
            size = random.randint(3, 5)  # Room size

            for i in range(size + 1):
                for j in range(size + 1):
                    carve_corridor(x + i, y, x + i + (random.choice([0, 1]) - 0.5), y + (random.choice([0, 1]) - 0.5))

    # Initialize the grid with walls
    grid = [["#"] * width for _ in range(height)]

    # Start corridor carving
    start_x, start_y = random.randint(0, width - 2), random.randint(0, height - 2)
    direction = random.choice(['N', 'S', 'E', 'W'])
    if direction == 'N':
        end_y = start_y + random.randint(3, 5)
    elif direction == 'S':
        end_y = start_y - random.randint(3, 5)
    elif direction == 'E':
        end_x = start_x + random.randint(3, 5)
    else:  # W
        end_x = start_x - random.randint(3, 5)

    carve_corridor(start_x, start_y, end_x, end_y)

    place_rooms()

    return grid


def print_dungeon(grid: List[List[str]]) -> None:
    """Print the generated dungeon."""
    for row in grid:
        print(''.join(row))


if __name__ == "__main__":
    dungeon = generate_dungeon()
    print_dungeon(dungeon)