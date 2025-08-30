import random

# Constants for dungeon generation
ROOM_MIN_SIZE = 2
ROOM_MAX_SIZE = 5
CORRIDOR_MIN_LENGTH = 1
CORRIDOR_MAX_LENGTH = 3
DUNGEON_WIDTH = 40
DUNGEON_HEIGHT = 20
WALL = '#'
FLOOR = ' '

def generate_room(x, y):
    size = random.randint(ROOM_MIN_SIZE, ROOM_MAX_SIZE)
    return [(x + i * (size + 1), y) for i in range(size)]

def place_rooms(dungeon, rooms):
    for room in rooms:
        x, y = room
        dungeon[y][x] = FLOOR
        # Place walls around the room
        for dx in [-1, 0, 1]:
            nx, ny = x + dx, y
            if not (0 <= nx < DUNGEON_WIDTH and dungeon[ny][nx] == FLOOR):
                continue
            dungeon[y - 1][nx], dungeon[y + 1][nx] = '#', '#'
        for dy in [-1, 0, 1]:
            nx, ny = x, y + dy
            if not (0 <= ny < DUNGEON_HEIGHT and dungeon[ny][nx] == FLOOR):
                continue
            dungeon[ny][x], dungeon[ny][x + size] = '#', '#'

def generate_corridors(dungeon, rooms):
    for x in range(DUNGEON_WIDTH):
        for y in range(DUNGEON_HEIGHT):
            if dungeon[y][x] == FLOOR:
                add_corridor(dungeon, (x, y))

def add_corridor(dungeon, start):
    x, y = start
    length = random.randint(CORRIDOR_MIN_LENGTH, CORRIDOR_MAX_LENGTH)

    dx, dy = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
    nx, ny = x + dx * length, y + dy * length

    while not (0 <= nx < DUNGEON_WIDTH and dungeon[ny][nx] == FLOOR):
        length += 1
        nx, ny = x + dx * length, y + dy * length

    for i in range(length):
        dungeon[y + dy * i][x + dx * i] = '#'

def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(row))

def create_dungeon():
    dungeon = [['#'] * DUNGEON_WIDTH for _ in range(DUNGEON_HEIGHT)]

    # Generate initial rooms
    rooms = [generate_room(random.randint(1, DUNGEON_WIDTH - 2), random.randint(1, DUNGEON_HEIGHT - 2))
              for _ in range(random.randint(3, 7))]
    place_rooms(dungeon, rooms)

    # Generate corridors
    generate_corridors(dungeon, rooms)

    return dungeon

if __name__ == "__main__":
    dungeon = create_dungeon()
    print_dungeon(dungeon)