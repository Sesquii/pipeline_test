import random

# Constants for the dungeon dimensions and symbols
WIDTH = 40
HEIGHT = 20
EMPTY = ' '
WALL = '#'
FLOOR = '.'
DOOR = '+'

def create_empty_dungeon():
    """Create an empty dungeon grid filled with walls."""
    return [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]

def place_room(dungeon, x, y, width, height):
    """Place a room in the dungeon at coordinates (x, y) with given dimensions."""
    for i in range(y, y + height):
        for j in range(x, x + width):
            if 0 <= i < HEIGHT and 0 <= j < WIDTH:
                dungeon[i][j] = FLOOR

def carve_corridor(dungeon, start_x, start_y, end_x, end_y):
    """Carve a corridor between two points (start_x, start_y) to (end_x, end_y)."""
    x, y = start_x, start_y
    while x != end_x or y != end_y:
        if x < end_x:
            x += 1
        elif x > end_x:
            x -= 1
        elif y < end_y:
            y += 1
        elif y > end_y:
            y -= 1

        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            dungeon[y][x] = FLOOR

def print_dungeon(dungeon):
    """Print the dungeon grid to the console."""
    for row in dungeon:
        print(''.join(row))

def generate_dungeon(num_rooms):
    """Generate a dungeon with a specified number of rooms."""
    dungeon = create_empty_dungeon()
    rooms = []

    for _ in range(num_rooms):
        width = random.randint(5, 10)
        height = random.randint(3, 6)
        x = random.randint(2, WIDTH - width - 2)
        y = random.randint(2, HEIGHT - height - 2)

        place_room(dungeon, x, y, width, height)
        rooms.append((x + width // 2, y + height // 2))

    # Connect rooms with corridors
    for i in range(len(rooms) - 1):
        carve_corridor(dungeon, *rooms[i], *rooms[i + 1])

    return dungeon

if __name__ == "__main__":
    num_rooms = 5  # You can adjust the number of rooms as needed
    dungeon = generate_dungeon(num_rooms)
    print_dungeon(dungeon)