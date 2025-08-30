```python
import sys
import random

def main():
    if len(sys.argv) < 3:
        print("Usage: python BATCH6_PROMPT2_{{model_name}}.py steps size")
        return
    
    steps = int(sys.argv[1])
    size_str = sys.argv[2]
    
    # Parse the map dimensions
    rows, cols = map(int, size_str.split('x'))
    
    # Initialize grid with walls ('+') and empty spaces (' ')
    grid = [['+' for _ in range(cols)] for _ in range(rows)]
    
    # Track visited cells
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    current_x, current_y = 0, 0
    visited[current_x][current_y] = True
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for _ in range(steps):
        dir_idx = random.randint(0, 3)
        dx, dy = directions[dir_idx]
        new_x = current_x + dx
        new_y = current_y + dy
        
        if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:
            # Move to the new cell if valid
            visited[new_x][new_y] = True
            grid[new_x][new_y] = ' '
            current_x, current_y = new_x, new_y
    
    # Print the dungeon map
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO
import sys

# Original code
def main():
    if len(sys.argv) < 3:
        print("Usage: python BATCH6_PROMPT2_{{model_name}}.py steps size")
        return
    
    steps = int(sys.argv[1])
    size_str = sys.argv[2]
    
    # Parse the map dimensions
    rows, cols = map(int, size_str.split('x'))
    
    # Initialize grid with walls ('+') and empty spaces (' ')
    grid = [['+' for _ in range(cols)] for _ in range(rows)]
    
    # Track visited cells
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    current_x, current_y = 0, 0
    visited[current_x][current_y] = True
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for _ in range(steps):
        dir_idx = random.randint(0, 3)
        dx, dy = directions[dir_idx]
        new_x = current_x + dx
        new_y = current_y + dy
        
        if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_x][new_y]:
            # Move to the new cell if valid
            visited[new_x][new_y] = True
            grid[new_x][new_y] = ' '
            current_x, current_y = new_x, new_y
    
    # Print the dungeon map
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()

# Test cases
def test_main(capsys):
    """Test the main function with valid input."""
    sys.argv = ["script.py", "10", "5x5"]
    main()
    captured = capsys.readouterr()
    assert len(captured.out.strip().split('\n')) == 5

def test_main_invalid_steps(capsys):
    """Test the main function with invalid steps input."""
    sys.argv = ["script.py", "-1", "5x5"]
    main()
    captured = capsys.readouterr()
    assert "Usage" in captured.out

def test_main_invalid_size(capsys):
    """Test the main function with invalid size input."""
    sys.argv = ["script.py", "10", "abc"]
    main()
    captured = capsys.readouterr()
    assert "Usage" in captured.out

def test_main_empty_steps(capsys):
    """Test the main function with empty steps input."""
    sys.argv = ["script.py", "", "5x5"]
    main()
    captured = capsys.readouterr()
    assert "Usage" in captured.out

def test_main_empty_size(capsys):
    """Test the main function with empty size input."""
    sys.argv = ["script.py", "10", ""]
    main()
    captured = capsys.readouterr()
    assert "Usage" in captured.out

def test_main_missing_args(capsys):
    """Test the main function with missing arguments."""
    sys.argv = ["script.py"]
    main()
    captured = capsys.readouterr()
    assert "Usage" in captured.out
```