```python
import sys

def main():
    # Initialize a 10x10 grid filled with walls
    grid = [['#'] * 10 for _ in range(10)]
    
    def generate(x1, y1, x2, y2):
        # Fill the current area with walls
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = '#'
        
        # Split into two halves and generate recursively
        mid_x = (x1 + x2) // 2
        if mid_x > x1:
            generate(x1, y1, mid_x - 1, y2)
        if mid_x < x2:
            generate(mid_x, y1, x2, y2)
        
        # Add a corridor between the two halves
        for i in range(mid_x, x2):
            grid[i][y1] = ' '
    
    generate(0, 0, 9, 9)
    
    # Print the dungeon map
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()