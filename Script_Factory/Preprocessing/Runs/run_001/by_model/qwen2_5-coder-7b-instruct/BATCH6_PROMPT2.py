import sys

def drunkards_walk(steps, width, height):
    # Initialize the dungeon with walls
    dungeon = [['+' for _ in range(width)] for _ in range(height)]
    
    # Starting point at the center of the dungeon
    x, y = width // 2, height // 2
    
    # Directions: right, up, left, down
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    
    for _ in range(steps):
        # Choose a random direction
        dx, dy = directions[sys.rand() % len(directions)]
        
        # Move to the new position
        nx, ny = x + dx, y + dy
        
        # Check if the new position is within bounds and not already a floor
        if 0 <= nx < width and 0 <= ny < height and dungeon[ny][nx] == '+':
            # Carve out a floor at the new position
            dungeon[ny][nx] = ' '
            
            # Move to the new position
            x, y = nx, ny
    
    return dungeon

def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(row))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python BATCH6_PROMPT2_{{model_name}}.py <steps> <width> <height>")
        sys.exit(1)
    
    steps = int(sys.argv[1])
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    
    dungeon = drunkards_walk(steps, width, height)
    print_dungeon(dungeon)
```

Save this code as `BATCH6_PROMPT2_{{model_name}}.py` and run it from the command line with the required arguments to generate and print a procedural dungeon using the drunkard's walk algorithm.