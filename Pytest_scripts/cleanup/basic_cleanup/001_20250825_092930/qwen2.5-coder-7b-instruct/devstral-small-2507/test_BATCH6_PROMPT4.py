# BATCH6_PROMPT4_Devstral.py

import random

def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(row))

def carve_passage(dungeon, x, y, direction):
    dx, dy = direction
    nx, ny = x + dx, y + dy

    if 0 <= nx < len(dungeon[0]) and 0 <= ny < len(dungeon):
        if dungeon[ny][nx] == '#':
            dungeon[ny][nx] = '.'
            return [(nx, ny)]
        else:
            return []

    return []

def grow_tree(dungeon, start_x, start_y):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_positions = [(start_x, start_y)]

    while current_positions:
        x, y = random.choice(current_positions)
        dungeon[y][x] = '.'

        valid_directions = [d for d in directions
                           if 0 <= x + d[0] < len(dungeon[0])
                           and 0 <= y + d[1] < len(dungeon)
                           and dungeon[y + d[1]][x + d[0]] == '#']

        if valid_directions:
            direction = random.choice(valid_directions)
            new_positions = carve_passage(dungeon, x, y, direction)
            current_positions.extend(new_positions)

        current_positions.remove((x, y))

def generate_dungeon(width, height):
    dungeon = [['#' for _ in range(width)] for _ in range(height)]
    start_x, start_y = width // 2, height // 2
    grow_tree(dungeon, start_x, start_y)
    return dungeon

if __name__ == "__main__":
    WIDTH = 40
    HEIGHT = 20
    dungeon = generate_dungeon(WIDTH, HEIGHT)
    print_dungeon(dungeon)

# ===== GENERATED TESTS =====
import pytest

# BATCH6_PROMPT4_Devstral.py

import random

def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(row))

def carve_passage(dungeon, x, y, direction):
    dx, dy = direction
    nx, ny = x + dx, y + dy

    if 0 <= nx < len(dungeon[0]) and 0 <= ny < len(dungeon):
        if dungeon[ny][nx] == '#':
            dungeon[ny][nx] = '.'
            return [(nx, ny)]
        else:
            return []

    return []

def grow_tree(dungeon, start_x, start_y):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_positions = [(start_x, start_y)]

    while current_positions:
        x, y = random.choice(current_positions)
        dungeon[y][x] = '.'

        valid_directions = [d for d in directions
                           if 0 <= x + d[0] < len(dungeon[0])
                           and 0 <= y + d[1] < len(dungeon)
                           and dungeon[y + d[1]][x + d[0]] == '#']

        if valid_directions:
            direction = random.choice(valid_directions)
            new_positions = carve_passage(dungeon, x, y, direction)
            current_positions.extend(new_positions)

        current_positions.remove((x, y))

def generate_dungeon(width, height):
    dungeon = [['#' for _ in range(width)] for _ in range(height)]
    start_x, start_y = width // 2, height // 2
    grow_tree(dungeon, start_x, start_y)
    return dungeon

if __name__ == "__main__":
    WIDTH = 40
    HEIGHT = 20
    dungeon = generate_dungeon(WIDTH, HEIGHT)
    print_dungeon(dungeon)

# Test suite for BATCH6_PROMPT4_Devstral.py

def test_carve_passage():
    """Test the carve_passage function."""
    dungeon = [['#' for _ in range(5)] for _ in range(5)]
    x, y, direction = 2, 2, (0, 1)
    result = carve_passage(dungeon, x, y, direction)
    assert result == [(2, 3)], f"Expected [(2, 3)], got {result}"
    assert dungeon[2][3] == '.', f"Dungeon at (2, 3) should be '.', got {dungeon[2][3]}"

def test_grow_tree():
    """Test the grow_tree function."""
    dungeon = [['#' for _ in range(5)] for _ in range(5)]
    start_x, start_y = 2, 2
    grow_tree(dungeon, start_x, start_y)
    assert dungeon[2][2] == '.', f"Dungeon at (2, 2) should be '.', got {dungeon[2][2]}"

def test_generate_dungeon():
    """Test the generate_dungeon function."""
    width, height = 5, 5
    dungeon = generate_dungeon(width, height)
    assert len(dungeon) == height, f"Dungeon height should be {height}, got {len(dungeon)}"
    assert len(dungeon[0]) == width, f"Dungeon width should be {width}, got {len(dungeon[0])}"
    assert dungeon[2][2] == '.', f"Dungeon at (2, 2) should be '.', got {dungeon[2][2]}"

def test_print_dungeon():
    """Test the print_dungeon function."""
    dungeon = [['#' for _ in range(5)] for _ in range(5)]
    with pytest.raises(SystemExit):
        print_dungeon(dungeon)

# Test fixtures and parametrization

@pytest.fixture
def sample_dungeon():
    return [['#' for _ in range(5)] for _ in range(5)]

@pytest.mark.parametrize("direction, expected", [
    ((0, 1), [(2, 3)]),
    ((1, 0), [(3, 2)]),
    ((0, -1), [(2, 1)]),
    ((-1, 0), [(1, 2)])
])
def test_carve_passage_with_direction(sample_dungeon, direction, expected):
    """Test the carve_passage function with different directions."""
    x, y = 2, 2
    result = carve_passage(sample_dungeon, x, y, direction)
    assert result == expected, f"Expected {expected}, got {result}"
    assert sample_dungeon[2][3] == '.', f"Dungeon at (2, 3) should be '.', got {sample_dungeon[2][3]}"

@pytest.mark.parametrize("width, height", [
    (5, 5),
    (10, 10),
    (20, 20)
])
def test_generate_dungeon_with_size(width, height):
    """Test the generate_dungeon function with different sizes."""
    dungeon = generate_dungeon(width, height)
    assert len(dungeon) == height, f"Dungeon height should be {height}, got {len(dungeon)}"
    assert len(dungeon[0]) == width, f"Dungeon width should be {width}, got {len(dungeon[0])}"
    assert dungeon[2][2] == '.', f"Dungeon at (2, 2) should be '.', got {dungeon[2][2]}"
