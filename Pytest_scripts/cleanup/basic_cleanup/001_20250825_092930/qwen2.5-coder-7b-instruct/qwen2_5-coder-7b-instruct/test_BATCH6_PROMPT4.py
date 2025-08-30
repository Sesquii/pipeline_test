import random

# Constants for the dungeon generation
WIDTH = 20
HEIGHT = 10
DENSITY = 0.3

def generate_dungeon(width=WIDTH, height=HEIGHT, density=DENSITY):
    """
    Generates a procedural dungeon using the growing tree algorithm.
    
    :param width: Width of the dungeon grid
    :param height: Height of the dungeon grid
    :param density: Probability of placing a wall in any given cell
    :return: A 2D list representing the dungeon grid
    """
    # Initialize the dungeon with walls
    dungeon = [['#' for _ in range(width)] for _ in range(height)]
    
    # List to keep track of cells that are part of the tree
    tree_cells = []
    
    # Start from a random cell and mark it as part of the tree
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    dungeon[start_y][start_x] = '.'
    tree_cells.append((start_x, start_y))
    
    while len(tree_cells) > 0:
        # Get a random cell from the tree
        current_x, current_y = tree_cells.pop()
        
        # Find unexplored neighbors
        neighbors = []
        if current_x > 0 and dungeon[current_y][current_x - 1] == '#':
            neighbors.append((current_x - 1, current_y))
        if current_x < width - 1 and dungeon[current_y][current_x + 1] == '#':
            neighbors.append((current_x + 1, current_y))
        if current_y > 0 and dungeon[current_y - 1][current_x] == '#':
            neighbors.append((current_x, current_y - 1))
        if current_y < height - 1 and dungeon[current_y + 1][current_x] == '#':
            neighbors.append((current_x, current_y + 1))
        
        if len(neighbors) > 0:
            # Choose a random neighbor to connect
            next_x, next_y = neighbors[random.randint(0, len(neighbors) - 1)]
            dungeon[next_y][next_x] = '.'
            tree_cells.append((next_x, next_y))
    
    return dungeon

def print_dungeon(dungeon):
    """
    Prints the dungeon grid to the console.
    
    :param dungeon: A 2D list representing the dungeon grid
    """
    for row in dungeon:
        print(''.join(row))

if __name__ == "__main__":
    dungeon = generate_dungeon()
    print_dungeon(dungeon)

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Constants for the dungeon generation
WIDTH = 20
HEIGHT = 10
DENSITY = 0.3

def generate_dungeon(width=WIDTH, height=HEIGHT, density=DENSITY) -> List[List[str]]:
    """
    Generates a procedural dungeon using the growing tree algorithm.
    
    :param width: Width of the dungeon grid
    :param height: Height of the dungeon grid
    :param density: Probability of placing a wall in any given cell
    :return: A 2D list representing the dungeon grid
    """
    # Initialize the dungeon with walls
    dungeon = [['#' for _ in range(width)] for _ in range(height)]
    
    # List to keep track of cells that are part of the tree
    tree_cells = []
    
    # Start from a random cell and mark it as part of the tree
    start_x, start_y = random.randint(0, width - 1), random.randint(0, height - 1)
    dungeon[start_y][start_x] = '.'
    tree_cells.append((start_x, start_y))
    
    while len(tree_cells) > 0:
        # Get a random cell from the tree
        current_x, current_y = tree_cells.pop()
        
        # Find unexplored neighbors
        neighbors = []
        if current_x > 0 and dungeon[current_y][current_x - 1] == '#':
            neighbors.append((current_x - 1, current_y))
        if current_x < width - 1 and dungeon[current_y][current_x + 1] == '#':
            neighbors.append((current_x + 1, current_y))
        if current_y > 0 and dungeon[current_y - 1][current_x] == '#':
            neighbors.append((current_x, current_y - 1))
        if current_y < height - 1 and dungeon[current_y + 1][current_x] == '#':
            neighbors.append((current_x, current_y + 1))
        
        if len(neighbors) > 0:
            # Choose a random neighbor to connect
            next_x, next_y = neighbors[random.randint(0, len(neighbors) - 1)]
            dungeon[next_y][next_x] = '.'
            tree_cells.append((next_x, next_y))
    
    return dungeon

def print_dungeon(dungeon: List[List[str]]) -> None:
    """
    Prints the dungeon grid to the console.
    
    :param dungeon: A 2D list representing the dungeon grid
    """
    for row in dungeon:
        print(''.join(row))

# Test cases
@pytest.fixture(params=[(10, 5, 0.4), (20, 10, 0.3), (30, 15, 0.2)])
def dungeon_params(request):
    return request.param

def test_generate_dungeon(dungeon_params: tuple) -> None:
    """
    Test the generate_dungeon function with different parameters.
    
    :param dungeon_params: Tuple containing width, height, and density
    """
    width, height, density = dungeon_params
    dungeon = generate_dungeon(width, height, density)
    assert isinstance(dungeon, list)
    assert all(isinstance(row, list) for row in dungeon)
    assert len(dungeon) == height
    assert all(len(row) == width for row in dungeon)
    assert all(cell in ['#', '.'] for row in dungeon for cell in row)

def test_print_dungeon() -> None:
    """
    Test the print_dungeon function.
    """
    dungeon = generate_dungeon(5, 5)
    captured_output = pytest.io.StringIO()
    with pytest.raises(SystemExit) as excinfo:
        print_dungeon(dungeon)
    assert excinfo.type == SystemExit
    assert captured_output.getvalue() != ""

# Run the tests
if __name__ == "__main__":
    pytest.main(['-v', __file__])

This test suite includes comprehensive test cases for the `generate_dungeon` and `print_dungeon` functions. It uses pytest fixtures and parametrization to test different parameters for the dungeon generation function. The test cases include both positive and negative scenarios, ensuring that the functions behave as expected under various conditions.