import random

# Constants for dungeon generation
WALL = '#'
PATH = ' '
DOOR = '+'

def print_dungeon(dungeon):
    """Print the dungeon map to the console."""
    for row in dungeon:
        print(''.join(row))

def generate_dungeon(width, height):
    """Generate a random dungeon using recursive division algorithm."""
    # Initialize the dungeon with walls
    dungeon = [[WALL for _ in range(width)] for _ in range(height)]

    def divide_room(x1, y1, x2, y2):
        """Divide the room recursively and create paths."""
        # Calculate room dimensions
        width = x2 - x1 + 1
        height = y2 - y1 + 1

        if width < 2 or height < 2:
            return

        # Randomly choose horizontal or vertical division
        if width > height:
            # Horizontal division
            wx = random.randint(x1, x2)
            wy = random.choice(range(y1, y2 + 1))

            # Create door at random position in the wall
            door_x = random.randint(max(x1, wx - 1), min(x2, wx + 1))
            dungeon[wy][door_x] = DOOR

            # Fill the path
            for x in range(min(x1, wx), max(x1, wx) + 1):
                if x != door_x:
                    dungeon[wy][x] = PATH

            # Recursively divide the rooms
            divide_room(x1, y1, wx - 1, y2)
            divide_room(wx + 1, y1, x2, y2)

        else:
            # Vertical division
            wy = random.randint(y1, y2)
            wx = random.choice(range(x1, x2 + 1))

            # Create door at random position in the wall
            door_y = random.randint(max(y1, wy - 1), min(y2, wy + 1))
            dungeon[door_y][wx] = DOOR

            # Fill the path
            for y in range(min(y1, wy), max(y1, wy) + 1):
                if y != door_y:
                    dungeon[y][wx] = PATH

            # Recursively divide the rooms  
            divide_room(x1, y1, x2, wy - 1)
            divide_room(x1, wy + 1, x2, y2)

    # Start dividing from the full dungeon
    divide_room(0, 0, width - 1, height - 1)

    return dungeon

def main():
    """Main function to generate and display the dungeon."""
    width = 40  # Dungeon width
    height = 20  # Dungeon height

    print("Generating dungeon...")
    dungeon = generate_dungeon(width, height)
    print_dungeon(dungeon)

if __name__ == "__main__":
    main()