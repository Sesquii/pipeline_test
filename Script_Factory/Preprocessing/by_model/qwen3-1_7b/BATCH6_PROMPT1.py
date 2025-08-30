```python
import sys

def generate_dungeon(rows=20, cols=20):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    
    # Initial walls placed in a 10x10 area
    for i in range(10):
        for j in range(10):
            grid[i][j] = '#'
    
    # Apply cellular automata rules to generate the dungeon
    for _ in range(20):  # Number of iterations to evolve the map
        new_grid = [['.' for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                count = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < rows and 0 <= nj < cols:
                            if grid[ni][nj] == '#':
                                count += 1
                if count >= 2:
                    new_grid[i][j] = '#'
                else:
                    new_grid[i][j] = '.'
        grid = new_grid
    
    return grid

if __name__ == "__main__":
    dungeon = generate_dungeon()
    for row in dungeon:
        print(''.join(row))