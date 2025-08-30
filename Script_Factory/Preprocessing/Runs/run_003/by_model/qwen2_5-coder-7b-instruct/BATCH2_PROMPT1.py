import random

def recursive_division(x1, y1, x2, y2, dungeon):
    # Base case: if the room is too small to subdivide
    if x2 - x1 <= 2 or y2 - y1 <= 2:
        return

    # Choose a random axis and position for division
    if random.choice([True, False]):
        # Horizontal division
        x_mid = random.randint(x1 + 2, x2 - 2)
        dungeon[y1][x_mid] = '#'
        for y in range(y1 + 1, y2):
            dungeon[y][x_mid] = '.'
        recursive_division(x1, y1, x_mid, y2, dungeon)
        recursive_division(x_mid, y1, x2, y2, dungeon)
    else:
        # Vertical division
        y_mid = random.randint(y1 + 2, y2 - 2)
        dungeon[y_mid][x1] = '#'
        for x in range(x1 + 1, x2):
            dungeon[y_mid][x] = '.'
        recursive_division(x1, y1, x2, y_mid, dungeon)
        recursive_division(x1, y_mid, x2, y2, dungeon)

def generate_dungeon(width, height):
    # Initialize the dungeon with walls
    dungeon = [['#' for _ in range(width)] for _ in range(height)]
    
    # Start recursive division from the top-left corner
    recursive_division(0, 0, width, height, dungeon)
    
    return dungeon

def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(row))

if __name__ == "__main__":
    width = 20
    height = 15
    dungeon = generate_dungeon(width, height)
    print_dungeon(dungeon)
```
This Python script generates a procedural dungeon map using the recursive division algorithm. The dungeon is represented as a grid of characters where `#` represents walls and `.` represents open spaces. The script includes functions for generating and printing the dungeon, with the main execution point defined in the `if __name__ == "__main__":` block.