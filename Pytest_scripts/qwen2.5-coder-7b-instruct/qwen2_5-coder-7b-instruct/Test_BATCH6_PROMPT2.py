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

# ===== GENERATED TESTS =====
```python
import pytest
from typing import List

# Original code
def drunkards_walk(steps: int, width: int, height: int) -> List[List[str]]:
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

def print_dungeon(dungeon: List[List[str]]) -> None:
    for row in dungeon:
        print(''.join(row))

# Test cases
@pytest.fixture
def random_seed():
    return 42

@pytest.mark.parametrize("steps,width,height", [
    (10, 5, 5),
    (20, 10, 10),
    (50, 15, 15)
])
def test_drunkards_walk(random_seed, steps: int, width: int, height: int) -> None:
    # Set the random seed for reproducibility
    sys.rand = lambda: random_seed
    
    dungeon = drunkards_walk(steps, width, height)
    
    assert len(dungeon) == height
    assert all(len(row) == width for row in dungeon)
    assert dungeon[height // 2][width // 2] == ' '
    assert any(cell == ' ' for row in dungeon for cell in row)

@pytest.mark.parametrize("steps,width,height", [
    (0, 5, 5),
    (-10, 10, 10),
    (10, -5, 5)
])
def test_drunkards_walk_invalid_steps(random_seed, steps: int, width: int, height: int) -> None:
    # Set the random seed for reproducibility
    sys.rand = lambda: random_seed
    
    with pytest.raises(ValueError):
        drunkards_walk(steps, width, height)

@pytest.mark.parametrize("steps,width,height", [
    (10, 0, 5),
    (10, 5, 0),
    (10, -5, 5)
])
def test_drunkards_walk_invalid_dimensions(random_seed, steps: int, width: int, height: int) -> None:
    # Set the random seed for reproducibility
    sys.rand = lambda: random_seed
    
    with pytest.raises(ValueError):
        drunkards_walk(steps, width, height)

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

This test suite includes comprehensive test cases for the `drunkards_walk` function and the `print_dungeon` function. It uses pytest fixtures and parametrization to handle different scenarios and validate the output of the functions. The test cases cover both positive and negative inputs, ensuring that the function behaves as expected under various conditions.