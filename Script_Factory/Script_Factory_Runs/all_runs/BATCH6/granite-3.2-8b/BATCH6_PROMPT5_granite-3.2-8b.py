import random
from collections import namedtuple

# Define Room and GridCell as named tuples for better readability
Room = namedtuple('Room', 'x, y, width, height')
GridCell = namedtuple('GridCell', 'is_wall, room')

def generate_dungeon(width, height):
    """Generates a dungeon of given dimensions."""

    # Initialize grid with walls
    cells = [[GridCell(True, None) for _ in range(width)] for _ in range(height)]

    def place_room(x, y, width, height):
        """Places a room at the specified coordinates and size."""
        for i in range(y, y + height):
            for j in range(x, x + width):
                cells[i][j] = GridCell(False, Room(x, y, width, height))

    def connect_corridors():
        """Connects rooms with corridors."""
        # Connect horizontally
        for y in range(height):
            for x in range(width - 1):
                if cells[y][x].is_wall and cells[y][x + 1].room:
                    connect_rooms(cells[y][x], cells[y][x + 1])

        # Connect vertically
        for x in range(width):
            for y in range(height - 1):
                if cells[y][x].is_wall and cells[y + 1][x].room:
                    connect_rooms(cells[y][x], cells[y + 1][x])

    def connect_rooms(room1, room2):
        """Connects two rooms with a corridor."""
        # Choose random start point for the corridor in the first room
        corridor_start = (random.randint(0, room1.width - 1), room1.y)

        # Check for valid path to second room
        dx, dy = room2.x - room1.x, room2.y - room1.y
        while (corridor_start[0] != dx or corridor_start[1] != dy):
            corridor_start = (corridor_start[0] + 1 if dx > 0 else corridor_start[0] - 1,
                               corridor_start[1] + 1 if dy > 0 else corridor_start[1] - 1)
            if not (0 <= corridor_start[0] < room1.width and 0 <= corridor_start[1] < room1.height):
                return

        # Create a corridor
        for i in range(corridor_start[0], dx + corridor_start[0]):
            cells[corridor_start[1]][i].is_wall = False

    # Generate rooms
    num_rooms = random.randint(8, 16)
    for _ in range(num_rooms):
        place_room(random.randint(0, width - 1),
                   random.randint(0, height - 2),   # Ensure there's space below for corridor
                   random.randint(3, 5),            # Room size variability
                   random.randint(3, 5))

    connect_corridors()

    return cells

def print_dungeon(cells):
    """Prints the dungeon in a text-based format."""
    for y, row in enumerate(cells):
        line = ''
        for x, cell in enumerate(row):
            if cell.is_wall:
                line += '#'  # Wall
            else:
                room = cell.room
                line += f'R{{x:{room.x}, y:{room.y}, w:{room.width}, h:{room.height}}}'
        print(line)

if __name__ == "__main__":
    dungeon_width, dungeon_height = 50, 30  # Set your desired dungeon size here
    dungeon = generate_dungeon(dungeon_width, dungeon_height)
    print_dungeon(dungeon)