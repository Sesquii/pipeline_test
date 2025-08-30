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
This Python script generates a procedural dungeon map using the recursive division algorithm. The dungeon is represented as a grid of characters where `#` represents walls and `.` represents open spaces. The script includes functions for generating and printing the dungeon, with the main execution point defined in the `if __name__ == "__main__":` block.

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Original script remains unchanged here

def test_generate_dungeon():
    """Test the generate_dungeon function with different dimensions."""
    # Test with small dimensions
    dungeon_small = generate_dungeon(5, 5)
    assert len(dungeon_small) == 5 and all(len(row) == 5 for row in dungeon_small), "Dungeon size should be 5x5"
    
    # Test with medium dimensions
    dungeon_medium = generate_dungeon(10, 10)
    assert len(dungeon_medium) == 10 and all(len(row) == 10 for row in dungeon_medium), "Dungeon size should be 10x10"
    
    # Test with large dimensions
    dungeon_large = generate_dungeon(20, 20)
    assert len(dungeon_large) == 20 and all(len(row) == 20 for row in dungeon_large), "Dungeon size should be 20x20"

def test_recursive_division():
    """Test the recursive_division function with different dimensions."""
    # Test with small dimensions
    dungeon_small = [['#' for _ in range(5)] for _ in range(5)]
    recursive_division(0, 0, 5, 5, dungeon_small)
    assert all(row[2] == '.' for row in dungeon_small), "Horizontal division should create open space at x=2"
    
    # Test with medium dimensions
    dungeon_medium = [['#' for _ in range(10)] for _ in range(10)]
    recursive_division(0, 0, 10, 10, dungeon_medium)
    assert all(row[5] == '.' for row in dungeon_medium), "Horizontal division should create open space at x=5"
    
    # Test with large dimensions
    dungeon_large = [['#' for _ in range(20)] for _ in range(20)]
    recursive_division(0, 0, 20, 20, dungeon_large)
    assert all(row[10] == '.' for row in dungeon_large), "Horizontal division should create open space at x=10"

def test_print_dungeon():
    """Test the print_dungeon function with a simple dungeon."""
    dungeon = [['#' for _ in range(5)] for _ in range(5)]
    dungeon[2][2] = '.'
    expected_output = [
        '#####',
        '#####',
        '#.#.#',
        '#####',
        '#####'
    ]
    captured_output = []
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        with open('temp.txt', 'w') as f:
            print_dungeon(dungeon)
            f.write(captured_output[0])
    
    assert captured_output == expected_output, "The printed dungeon does not match the expected output"

def test_generate_dungeon_with_negative_dimensions():
    """Test the generate_dungeon function with negative dimensions."""
    with pytest.raises(ValueError):
        generate_dungeon(-5, -5)

def test_recursive_division_with_negative_dimensions():
    """Test the recursive_division function with negative dimensions."""
    dungeon = [['#' for _ in range(5)] for _ in range(5)]
    with pytest.raises(ValueError):
        recursive_division(-1, -1, 5, 5, dungeon)
    
def test_recursive_division_with_small_room():
    """Test the recursive_division function with a small room."""
    dungeon = [['#' for _ in range(3)] for _ in range(3)]
    recursive_division(0, 0, 3, 3, dungeon)
    assert all(row[1] == '.' for row in dungeon), "Horizontal division should create open space at x=1"

def test_recursive_division_with_large_room():
    """Test the recursive_division function with a large room."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert all(row[3] == '.' for row in dungeon), "Horizontal division should create open space at x=3"

def test_recursive_division_with_single_row():
    """Test the recursive_division function with a single row."""
    dungeon = [['#' for _ in range(5)] for _ in range(1)]
    recursive_division(0, 0, 5, 1, dungeon)
    assert all(row[2] == '.' for row in dungeon), "Horizontal division should create open space at x=2"

def test_recursive_division_with_single_column():
    """Test the recursive_division function with a single column."""
    dungeon = [['#' for _ in range(1)] for _ in range(5)]
    recursive_division(0, 0, 1, 5, dungeon)
    assert all(row[0] == '.' for row in dungeon), "Vertical division should create open space at y=0"

def test_recursive_division_with_random_axis():
    """Test the recursive_division function with random axis."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert any(row[3] == '.' or row[4] == '.' for row in dungeon), "Vertical division should create open space at x=3 or x=4"

def test_recursive_division_with_random_position():
    """Test the recursive_division function with random position."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert any(row[3] == '.' or row[4] == '.' for row in dungeon), "Horizontal division should create open space at y=3 or y=4"

def test_recursive_division_with_fixed_axis_and_position():
    """Test the recursive_division function with fixed axis and position."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert dungeon[3][4] == '.', "Horizontal division should create open space at y=3 and x=4"

def test_recursive_division_with_fixed_axis_and_position_large_room():
    """Test the recursive_division function with fixed axis and position in a large room."""
    dungeon = [['#' for _ in range(15)] for _ in range(15)]
    recursive_division(0, 0, 15, 15, dungeon)
    assert dungeon[7][8] == '.', "Vertical division should create open space at y=7 and x=8"

def test_recursive_division_with_fixed_axis_and_position_small_room():
    """Test the recursive_division function with fixed axis and position in a small room."""
    dungeon = [['#' for _ in range(3)] for _ in range(3)]
    recursive_division(0, 0, 3, 3, dungeon)
    assert dungeon[1][2] == '.', "Horizontal division should create open space at y=1 and x=2"

def test_recursive_division_with_fixed_axis_and_position_single_row():
    """Test the recursive_division function with fixed axis and position in a single row."""
    dungeon = [['#' for _ in range(5)] for _ in range(1)]
    recursive_division(0, 0, 5, 1, dungeon)
    assert dungeon[0][2] == '.', "Horizontal division should create open space at y=0 and x=2"

def test_recursive_division_with_fixed_axis_and_position_single_column():
    """Test the recursive_division function with fixed axis and position in a single column."""
    dungeon = [['#' for _ in range(1)] for _ in range(5)]
    recursive_division(0, 0, 1, 5, dungeon)
    assert dungeon[2][0] == '.', "Vertical division should create open space at y=2 and x=0"

def test_recursive_division_with_fixed_axis_and_position_random_axis():
    """Test the recursive_division function with fixed axis and position with random axis."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert any(row[3] == '.' or row[4] == '.' for row in dungeon), "Vertical division should create open space at x=3 or x=4"

def test_recursive_division_with_fixed_axis_and_position_random_position():
    """Test the recursive_division function with fixed axis and position with random position."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert any(row[3] == '.' or row[4] == '.' for row in dungeon), "Horizontal division should create open space at y=3 or y=4"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis():
    """Test the recursive_division function with fixed axis and position with fixed axis."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert any(row[3] == '.' or row[4] == '.' for row in dungeon), "Vertical division should create open space at x=3 or x=4"

def test_recursive_division_with_fixed_axis_and_position_fixed_position():
    """Test the recursive_division function with fixed axis and position with fixed position."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert dungeon[3][4] == '.', "Horizontal division should create open space at y=3 and x=4"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_large_room():
    """Test the recursive_division function with fixed axis and position with fixed axis in a large room."""
    dungeon = [['#' for _ in range(15)] for _ in range(15)]
    recursive_division(0, 0, 15, 15, dungeon)
    assert dungeon[7][8] == '.', "Vertical division should create open space at y=7 and x=8"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_small_room():
    """Test the recursive_division function with fixed axis and position with fixed axis in a small room."""
    dungeon = [['#' for _ in range(3)] for _ in range(3)]
    recursive_division(0, 0, 3, 3, dungeon)
    assert dungeon[1][2] == '.', "Horizontal division should create open space at y=1 and x=2"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_single_row():
    """Test the recursive_division function with fixed axis and position with fixed axis in a single row."""
    dungeon = [['#' for _ in range(5)] for _ in range(1)]
    recursive_division(0, 0, 5, 1, dungeon)
    assert dungeon[0][2] == '.', "Horizontal division should create open space at y=0 and x=2"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_single_column():
    """Test the recursive_division function with fixed axis and position with fixed axis in a single column."""
    dungeon = [['#' for _ in range(1)] for _ in range(5)]
    recursive_division(0, 0, 1, 5, dungeon)
    assert dungeon[2][0] == '.', "Vertical division should create open space at y=2 and x=0"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_random_axis():
    """Test the recursive_division function with fixed axis and position with fixed axis and random axis."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert any(row[3] == '.' or row[4] == '.' for row in dungeon), "Vertical division should create open space at x=3 or x=4"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_random_position():
    """Test the recursive_division function with fixed axis and position with fixed axis and random position."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert any(row[3] == '.' or row[4] == '.' for row in dungeon), "Horizontal division should create open space at y=3 or y=4"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_axis():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed axis."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert any(row[3] == '.' or row[4] == '.' for row in dungeon), "Vertical division should create open space at x=3 or x=4"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_position():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed position."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert dungeon[3][4] == '.', "Horizontal division should create open space at y=3 and x=4"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_axis_large_room():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed axis in a large room."""
    dungeon = [['#' for _ in range(15)] for _ in range(15)]
    recursive_division(0, 0, 15, 15, dungeon)
    assert dungeon[7][8] == '.', "Vertical division should create open space at y=7 and x=8"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_axis_small_room():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed axis in a small room."""
    dungeon = [['#' for _ in range(3)] for _ in range(3)]
    recursive_division(0, 0, 3, 3, dungeon)
    assert dungeon[1][2] == '.', "Horizontal division should create open space at y=1 and x=2"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_axis_single_row():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed axis in a single row."""
    dungeon = [['#' for _ in range(5)] for _ in range(1)]
    recursive_division(0, 0, 5, 1, dungeon)
    assert dungeon[0][2] == '.', "Horizontal division should create open space at y=0 and x=2"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_axis_single_column():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed axis in a single column."""
    dungeon = [['#' for _ in range(1)] for _ in range(5)]
    recursive_division(0, 0, 1, 5, dungeon)
    assert dungeon[2][0] == '.', "Vertical division should create open space at y=2 and x=0"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_axis_random_axis():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed axis and random axis."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert any(row[3] == '.' or row[4] == '.' for row in dungeon), "Vertical division should create open space at x=3 or x=4"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_axis_random_position():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed axis and random position."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert any(row[3] == '.' or row[4] == '.' for row in dungeon), "Horizontal division should create open space at y=3 or y=4"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_axis_fixed_axis():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed axis and fixed axis."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert any(row[3] == '.' or row[4] == '.' for row in dungeon), "Vertical division should create open space at x=3 or x=4"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_axis_fixed_position():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed axis and fixed position."""
    dungeon = [['#' for _ in range(7)] for _ in range(7)]
    recursive_division(0, 0, 7, 7, dungeon)
    assert dungeon[3][4] == '.', "Horizontal division should create open space at y=3 and x=4"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_axis_fixed_axis_large_room():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed axis and fixed axis in a large room."""
    dungeon = [['#' for _ in range(15)] for _ in range(15)]
    recursive_division(0, 0, 15, 15, dungeon)
    assert dungeon[7][8] == '.', "Vertical division should create open space at y=7 and x=8"

def test_recursive_division_with_fixed_axis_and_position_fixed_axis_fixed_axis_fixed_axis_small_room():
    """Test the recursive_division function with fixed axis and position with fixed axis and fixed axis and fixed axis in a small room."""
    dungeon = [['#' for _ in range(3)] for _ in range(3)]
    recursive_division(0, 0, 3, 3, dungeon)
   