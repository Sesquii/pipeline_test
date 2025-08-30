import random
from itertools import product

def create_empty_dungeon(width, height):
    """Generate an empty dungeon grid."""
    return [['.' for _ in range(width)] for _ in range(height)]

def generate_cellular_automata(dungeon, radius=3):
    """Apply cellular automaton rules to the dungeon."""
    new_dungeon = [[cell for cell in row] for row in dungeon]

    for y, x in product(range(len(dungeon)), range(len(dungeon[0]))):
        live_neighbors = sum(
            dungeon[dy][dx] == '#'
            for dy, dx in ((y-1, x-1), (y-1, x), (y-1, x+1),
                           (y, x-1), (y, x+1),
                           (y+1, x-1), (y+1, x), (y+1, x+1))
            if 0 <= dy < len(dungeon) and 0 <= dx < len(dungeon[0])
        )

        if dungeon[y][x] == '#':
            if live_neighbors < 2 or live_neighbors > 3:
                new_dungeon[y][x] = '.'
        else:
            if live_neighbors == 3:
                new_dungeon[y][x] = '#'

    return new_dungeon

def print_dungeon(dungeon):
    """Print the dungeon to console."""
    for row in dungeon:
        print(''.join(row))

def main():
    width, height = 50, 30
    dungeon = create_empty_dungeon(width, height)

    print("Generating Dungeon...")
    dungeon = generate_cellular_automata(dungeon)

    print("\nDungeon Generated:\n")
    print_dungeon(dungeon)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Original code
def create_empty_dungeon(width: int, height: int) -> List[List[str]]:
    """Generate an empty dungeon grid."""
    return [['.' for _ in range(width)] for _ in range(height)]

def generate_cellular_automata(dungeon: List[List[str]], radius: int = 3) -> List[List[str]]:
    """Apply cellular automaton rules to the dungeon."""
    new_dungeon = [[cell for cell in row] for row in dungeon]

    for y, x in product(range(len(dungeon)), range(len(dungeon[0]))):
        live_neighbors = sum(
            dungeon[dy][dx] == '#'
            for dy, dx in ((y-1, x-1), (y-1, x), (y-1, x+1),
                           (y, x-1), (y, x+1),
                           (y+1, x-1), (y+1, x), (y+1, x+1))
            if 0 <= dy < len(dungeon) and 0 <= dx < len(dungeon[0])
        )

        if dungeon[y][x] == '#':
            if live_neighbors < 2 or live_neighbors > 3:
                new_dungeon[y][x] = '.'
        else:
            if live_neighbors == 3:
                new_dungeon[y][x] = '#'

    return new_dungeon

def print_dungeon(dungeon: List[List[str]]) -> None:
    """Print the dungeon to console."""
    for row in dungeon:
        print(''.join(row))

def main():
    width, height = 50, 30
    dungeon = create_empty_dungeon(width, height)

    print("Generating Dungeon...")
    dungeon = generate_cellular_automata(dungeon)

    print("\nDungeon Generated:\n")
    print_dungeon(dungeon)

if __name__ == "__main__":
    main()

# Test cases
def test_create_empty_dungeon():
    """Test the create_empty_dungeon function."""
    width, height = 50, 30
    dungeon = create_empty_dungeon(width, height)
    assert len(dungeon) == height
    for row in dungeon:
        assert len(row) == width and all(cell == '.' for cell in row)

def test_generate_cellular_automata():
    """Test the generate_cellular_automata function."""
    # Test case 1: Empty dungeon
    empty_dungeon = create_empty_dungeon(3, 3)
    new_dungeon = generate_cellular_automata(empty_dungeon)
    assert new_dungeon == empty_dungeon

    # Test case 2: Single cell alive
    single_live_dungeon = [['.', '.', '.'], ['.', '#', '.'], ['.', '.', '.']]
    new_dungeon = generate_cellular_automata(single_live_dungeon)
    assert new_dungeon == [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

    # Test case 3: Single cell dead
    single_dead_dungeon = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
    new_dungeon = generate_cellular_automata(single_dead_dungeon)
    assert new_dungeon == [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

    # Test case 4: Glider pattern
    glider_dungeon = [
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '#', '.', '.'],
        ['.', '#', '#', '#', '.'],
        ['.', '.', '#', '.', '.']
    ]
    new_dungeon = generate_cellular_automata(glider_dungeon)
    expected_new_dungeon = [
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.']
    ]
    assert new_dungeon == expected_new_dungeon

def test_print_dungeon(capsys):
    """Test the print_dungeon function."""
    dungeon = [['.', '#', '.'], ['#', '#', '#']]
    print_dungeon(dungeon)
    captured = capsys.readouterr()
    assert captured.out.strip() == '..#\n###'
