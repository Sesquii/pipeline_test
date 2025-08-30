```python
import sys

def generate_dungeon(x1, y1, x2, y2):
    # Initialize a grid with walls (0) and open spaces (1)
    grid = [[0]*(x2 - x1 + 1) for _ in range(y2 - y1 + 1)]
    
    # Fill the current area with open spaces
    for i in range(y2 - y1 + 1):
        for j in range(x2 - x1 + 1):
            grid[i][j] = 1
    
    mid_x = (x1 + x2) // 2
    mid_y = (y1 + y2) // 2

    # Generate left and right quadrants
    generate_dungeon(x1, y1, mid_x - 1, y2)
    generate_dungeon(mid_x, y1, x2, y2)

    # Generate top and bottom quadrants
    generate_dungeon(x1, y1, mid_y - 1, y2)
    generate_dungeon(x1, y2, mid_y + 1, x2)

    return grid

def main():
    if len(sys.argv) < 2:
        print("Usage: python BATCH3_PROMPT1_{{model_name}}.py")
        sys.exit(1)
    
    # Create a dungeon of size 10x10
    dungeon = generate_dungeon(0, 0, 9, 9)
    for row in dungeon:
        print(''.join(['#' if cell == 0 else 'O' for cell in row]))

if __name__ == "__main__":
    main()