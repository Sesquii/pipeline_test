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

# ===== GENERATED TESTS =====
```python
import pytest
from typing import List

# Constants for dungeon generation
WALL = '#'
PATH = ' '
DOOR = '+'

def print_dungeon(dungeon: List[List[str]]) -> None:
    """Print the dungeon map to the console."""
    for row in dungeon:
        print(''.join(row))

def generate_dungeon(width: int, height: int) -> List[List[str]]:
    """Generate a random dungeon using recursive division algorithm."""
    # Initialize the dungeon with walls
    dungeon = [[WALL for _ in range(width)] for _ in range(height)]

    def divide_room(x1: int, y1: int, x2: int, y2: int) -> None:
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

# Test cases for the script

def test_generate_dungeon():
    """Test the generate_dungeon function."""
    width = 10
    height = 5
    dungeon = generate_dungeon(width, height)

    # Check if the dungeon is of the correct size
    assert len(dungeon) == height
    for row in dungeon:
        assert len(row) == width

    # Check if all walls are present at the edges
    for i in range(height):
        assert dungeon[i][0] == WALL
        assert dungeon[i][-1] == WALL
    for j in range(width):
        assert dungeon[0][j] == WALL
        assert dungeon[-1][j] == WALL

def test_generate_dungeon_with_negative_dimensions():
    """Test the generate_dungeon function with negative dimensions."""
    width = -5
    height = -3
    with pytest.raises(ValueError):
        generate_dungeon(width, height)

def test_generate_dungeon_with_zero_dimensions():
    """Test the generate_dungeon function with zero dimensions."""
    width = 0
    height = 0
    with pytest.raises(ValueError):
        generate_dungeon(width, height)

def test_generate_dungeon_with_small_dimensions():
    """Test the generate_dungeon function with small dimensions."""
    width = 2
    height = 2
    dungeon = generate_dungeon(width, height)

    # Check if the dungeon is of the correct size
    assert len(dungeon) == height
    for row in dungeon:
        assert len(row) == width

    # Check if all walls are present at the edges
    for i in range(height):
        assert dungeon[i][0] == WALL
        assert dungeon[i][-1] == WALL
    for j in range(width):
        assert dungeon[0][j] == WALL
        assert dungeon[-1][j] == WALL

def test_generate_dungeon_with_large_dimensions():
    """Test the generate_dungeon function with large dimensions."""
    width = 50
    height = 30
    dungeon = generate_dungeon(width, height)

    # Check if the dungeon is of the correct size
    assert len(dungeon) == height
    for row in dungeon:
        assert len(row) == width

    # Check if all walls are present at the edges
    for i in range(height):
        assert dungeon[i][0] == WALL
        assert dungeon[i][-1] == WALL
    for j in range(width):
        assert dungeon[0][j] == WALL
        assert dungeon[-1][j] == WALL

def test_generate_dungeon_with_random_dimensions():
    """Test the generate_dungeon function with random dimensions."""
    width = random.randint(5, 20)
    height = random.randint(5, 20)
    dungeon = generate_dungeon(width, height)

    # Check if the dungeon is of the correct size
    assert len(dungeon) == height
    for row in dungeon:
        assert len(row) == width

    # Check if all walls are present at the edges
    for i in range(height):
        assert dungeon[i][0] == WALL
        assert dungeon[i][-1] == WALL
    for j in range(width):
        assert dungeon[0][j] == WALL
        assert dungeon[-1][j] == WALL

def test_generate_dungeon_with_single_cell():
    """Test the generate_dungeon function with a single cell."""
    width = 1
    height = 1
    dungeon = generate_dungeon(width, height)

    # Check if the dungeon is of the correct size
    assert len(dungeon) == height
    for row in dungeon:
        assert len(row) == width

    # Check if the single cell is a path
    assert dungeon[0][0] == PATH

def test_generate_dungeon_with_no_division():
    """Test the generate_dungeon function with no division."""
    width = 2
    height = 2
    dungeon = generate_dungeon(width, height)

    # Check if the dungeon is of the correct size
    assert len(dungeon) == height
    for row in dungeon:
        assert len(row) == width

    # Check if all walls are present at the edges
    for i in range(height):
        assert dungeon[i][0] == WALL
        assert dungeon[i][-1] == WALL
    for j in range(width):
        assert dungeon[0][j] == WALL
        assert dungeon[-1][j] == WALL

def test_generate_dungeon_with_all_doors():
    """Test the generate_dungeon function with all doors."""
    width = 4
    height = 3
    dungeon = generate_dungeon(width, height)

    # Check if the dungeon is of the correct size
    assert len(dungeon) == height
    for row in dungeon:
        assert len(row) == width

    # Check if all walls are present at the edges
    for i in range(height):
        assert dungeon[i][0] == WALL
        assert dungeon[i][-1] == WALL
    for j in range(width):
        assert dungeon[0][j] == WALL
        assert dungeon[-1][j] == WALL

    # Check if all paths are present
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            assert dungeon[i][j] == PATH

def test_generate_dungeon_with_no_paths():
    """Test the generate_dungeon function with no paths."""
    width = 4
    height = 3
    dungeon = generate_dungeon(width, height)

    # Check if the dungeon is of the correct size
    assert len(dungeon) == height
    for row in dungeon:
        assert len(row) == width

    # Check if all walls are present at the edges
    for i in range(height):
        assert dungeon[i][0] == WALL
        assert dungeon[i][-1] == WALL
    for j in range(width):
        assert dungeon[0][j] == WALL
        assert dungeon[-1][j] == WALL

    # Check if all walls are present
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            assert dungeon[i][j] == WALL

def test_generate_dungeon_with_random_divisions():
    """Test the generate_dungeon function with random divisions."""
    width = random.randint(5, 20)
    height = random.randint(5, 20)
    dungeon = generate_dungeon(width, height)

    # Check if the dungeon is of the correct size
    assert len(dungeon) == height
    for row in dungeon:
        assert len(row) == width

    # Check if all walls are present at the edges
    for i in range(height):
        assert dungeon[i][0] == WALL
        assert dungeon[i][-1] == WALL
    for j in range(width):
        assert dungeon[0][j] == WALL
        assert dungeon[-1][j] == WALL

    # Check if there are paths and doors
    has_path = False
    has_door = False
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if dungeon[i][j] == PATH:
                has_path = True
            elif dungeon[i][j] == DOOR:
                has_door = True

    assert has_path
    assert has_door
```