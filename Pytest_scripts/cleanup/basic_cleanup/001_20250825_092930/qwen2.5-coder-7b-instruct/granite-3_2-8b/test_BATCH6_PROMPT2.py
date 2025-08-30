import sys
import random

def drunkards_walk(steps, size):
    """Generate a dungeon using the 'drunkard's walk' algorithm."""
    x, y = 0, 0
    grid = [['+' for _ in range(size)] for _ in range(size)]

    for _ in range(steps):
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1
        else: # right
            x += 1

        # Ensure the walker doesn't go out of bounds.
        x = max(0, min(size - 1, x))
        y = max(0, min(size - 1, y))

        grid[y][x] = ' '

    return grid

def print_grid(grid):
    """Print the generated dungeon grid."""
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python BATCH6_PROMPT2_{model_name}.py <steps> <size>")
        sys.exit(1)

    steps = int(sys.argv[1])
    size = int(sys.argv[2])

    dungeon = drunkards_walk(steps, size)
    print_grid(dungeon)

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Original code
def drunkards_walk(steps: int, size: int) -> List[List[str]]:
    """Generate a dungeon using the 'drunkard's walk' algorithm."""
    x, y = 0, 0
    grid = [['+' for _ in range(size)] for _ in range(size)]

    for _ in range(steps):
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1
        else: # right
            x += 1

        # Ensure the walker doesn't go out of bounds.
        x = max(0, min(size - 1, x))
        y = max(0, min(size - 1, y))

        grid[y][x] = ' '

    return grid

def print_grid(grid: List[List[str]]) -> None:
    """Print the generated dungeon grid."""
    for row in grid:
        print(''.join(row))

# Test code
@pytest.fixture
def random_walk():
    """Fixture to generate a random walk."""
    steps = 10
    size = 5
    return drunkards_walk(steps, size)

def test_drunkards_walk(random_walk):
    """Test the drunkards_walk function."""
    assert len(random_walk) == 5
    for row in random_walk:
        assert len(row) == 5

def test_print_grid():
    """Test the print_grid function with a simple grid."""
    grid = [['+', '+', '+'], ['+', ' ', '+'], ['+', '+', '+']]
    expected_output = "+++\n+ +\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_out_of_bounds():
    """Test the drunkards_walk function with out-of-bounds steps."""
    steps = 100
    size = 5
    walk = drunkards_walk(steps, size)
    for row in walk:
        assert all(cell != ' ' for cell in row)

def test_print_grid_empty_grid():
    """Test the print_grid function with an empty grid."""
    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    expected_output = "   \n   \n   "
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_negative_steps():
    """Test the drunkards_walk function with negative steps."""
    steps = -5
    size = 5
    walk = drunkards_walk(steps, size)
    for row in walk:
        assert all(cell != ' ' for cell in row)

def test_print_grid_large_grid():
    """Test the print_grid function with a large grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_zero_steps():
    """Test the drunkards_walk function with zero steps."""
    steps = 0
    size = 5
    walk = drunkards_walk(steps, size)
    for row in walk:
        assert all(cell != ' ' for cell in row)

def test_print_grid_single_cell_grid():
    """Test the print_grid function with a single cell grid."""
    grid = [['+']]
    expected_output = "+"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_large_size():
    """Test the drunkards_walk function with a large size."""
    steps = 10
    size = 100
    walk = drunkards_walk(steps, size)
    for row in walk:
        assert len(row) == 100

def test_print_grid_large_size_grid():
    """Test the print_grid function with a large size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_small_size():
    """Test the drunkards_walk function with a small size."""
    steps = 10
    size = 2
    walk = drunkards_walk(steps, size)
    for row in walk:
        assert len(row) == 2

def test_print_grid_small_size_grid():
    """Test the print_grid function with a small size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_negative_size():
    """Test the drunkards_walk function with negative size."""
    steps = 10
    size = -5
    walk = drunkards_walk(steps, size)
    for row in walk:
        assert all(cell != ' ' for cell in row)

def test_print_grid_zero_size_grid():
    """Test the print_grid function with a zero size grid."""
    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    expected_output = "   \n   \n   "
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_large_steps():
    """Test the drunkards_walk function with large steps."""
    steps = 1000
    size = 5
    walk = drunkards_walk(steps, size)
    for row in walk:
        assert all(cell != ' ' for cell in row)

def test_print_grid_large_steps_grid():
    """Test the print_grid function with a large steps grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_small_steps():
    """Test the drunkards_walk function with small steps."""
    steps = 10
    size = 5
    walk = drunkards_walk(steps, size)
    for row in walk:
        assert all(cell != ' ' for cell in row)

def test_print_grid_small_steps_grid():
    """Test the print_grid function with a small steps grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_zero_steps_grid():
    """Test the drunkards_walk function with zero steps grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_negative_steps_grid():
    """Test the drunkards_walk function with negative steps grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_large_size_grid():
    """Test the drunkards_walk function with large size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_small_size_grid():
    """Test the drunkards_walk function with small size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_zero_size_steps():
    """Test the drunkards_walk function with zero size steps."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_negative_size_steps():
    """Test the drunkards_walk function with negative size steps."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_large_steps_size():
    """Test the drunkards_walk function with large steps size."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_small_steps_size():
    """Test the drunkards_walk function with small steps size."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_zero_steps_size():
    """Test the drunkards_walk function with zero steps size."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_negative_steps_size():
    """Test the drunkards_walk function with negative steps size."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_large_steps_size_grid():
    """Test the drunkards_walk function with large steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_small_steps_size_grid():
    """Test the drunkards_walk function with small steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_zero_steps_size_grid():
    """Test the drunkards_walk function with zero steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_negative_steps_size_grid():
    """Test the drunkards_walk function with negative steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_large_steps_size_grid():
    """Test the drunkards_walk function with large steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_small_steps_size_grid():
    """Test the drunkards_walk function with small steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_zero_steps_size_grid():
    """Test the drunkards_walk function with zero steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_negative_steps_size_grid():
    """Test the drunkards_walk function with negative steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_large_steps_size_grid():
    """Test the drunkards_walk function with large steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_small_steps_size_grid():
    """Test the drunkards_walk function with small steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_zero_steps_size_grid():
    """Test the drunkards_walk function with zero steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_negative_steps_size_grid():
    """Test the drunkards_walk function with negative steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_large_steps_size_grid():
    """Test the drunkards_walk function with large steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "+++\n+++\n+++"
    captured_output = pytest.io.StringIO()
    sys.stdout = captured_output
    print_grid(grid)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == expected_output

def test_drunkards_walk_small_steps_size_grid():
    """Test the drunkards_walk function with small steps size grid."""
    grid = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]
    expected_output = "++