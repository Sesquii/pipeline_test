import random

# Constants for room dimensions and corridor width
MIN_ROOM_SIZE = 3
MAX_ROOM_SIZE = 6
CORRIDOR_WIDTH = 1

def create_dungeon(width, height):
    dungeon = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Place rooms on the grid
    rooms = []
    attempts = 0
    while len(rooms) < 5 and attempts < 100:  # Limit to 5 rooms with max attempts
        x = random.randint(0, width - MAX_ROOM_SIZE)
        y = random.randint(0, height - MAX_ROOM_SIZE)
        room_width = random.randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
        room_height = random.randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
        
        if all(dungeon[y + j][x + i] == ' ' for i in range(room_width) for j in range(room_height)):
            rooms.append((x, y, room_width, room_height))
            for i in range(x, x + room_width):
                for j in range(y, y + room_height):
                    dungeon[j][i] = '#'
            attempts = 0
        else:
            attempts += 1
    
    # Connect rooms with corridors
    for i in range(len(rooms) - 1):
        start_room = rooms[i]
        end_room = rooms[i + 1]
        
        if start_room[1] <= end_room[1]:  # Connect vertically
            x = random.randint(start_room[0], min(start_room[0] + start_room[2], end_room[0]))
            for y in range(start_room[1], end_room[1]):
                dungeon[y][x] = '-'
        else:  # Connect horizontally
            y = random.randint(start_room[1], min(start_room[1] + start_room[3], end_room[1]))
            for x in range(start_room[0], end_room[0]):
                dungeon[y][x] = '|'
    
    return dungeon

def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(row))

if __name__ == "__main__":
    width, height = 20, 10
    dungeon = create_dungeon(width, height)
    print_dungeon(dungeon)