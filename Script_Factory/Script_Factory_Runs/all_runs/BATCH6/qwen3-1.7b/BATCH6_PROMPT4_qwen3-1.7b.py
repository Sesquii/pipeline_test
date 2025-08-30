```python
import sys
from collections import deque

def generate_dungeon(size):
    grid = [['#' for _ in range(size)] for _ in range(size)]
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start_x, start_y = size // 2, size // 2
    grid[start_x][start_y] = '.'
    queue = deque([(start_x, start_y)])
    visited.add((start_x, start_y))
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and grid[nx][ny] == '#' and (nx, ny) not in visited:
                grid[nx][ny] = '.'
                queue.append((nx, ny))
                visited.add((nx, ny))
    
    return grid

def print_dungeon(grid):
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    size = 20
    dungeon = generate_dungeon(size)
    print_dungeon(dungeon)