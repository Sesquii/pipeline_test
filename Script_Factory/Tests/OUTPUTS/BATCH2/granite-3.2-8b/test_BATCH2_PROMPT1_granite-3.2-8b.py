import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from Script_Factory.Script_Factory_Runs.all_runs.BATCH2.granite-3.2-8b.BATCH2_PROMPT1_granite-3.2-8b import (
    create_room,
    draw_wall,
    recursive_divide,
    generate_dungeon,
    print_dungeon
)

import pytest

def test_create_room():
    """Test the create_room function with normal inputs."""
    room = create_room(10, 10)
    assert isinstance(room, tuple) and len(room) == 2
    assert all(isinstance(point, tuple) and len(point) == 2 for point in room)

def test_draw_wall():
    """Test the draw_wall function with normal inputs."""
    dungeon = [[' ' for _ in range(5)] for _ in range(5)]
    x1, y1 = 0, 0
    x2, y2 = 1, 1
    draw_wall(dungeon, x1, y1, x2, y2)
    assert dungeon[y1][x1] == '#' and dungeon[y2][x2] == '#'

def test_recursive_divide():
    """Test the recursive_divide function with normal inputs."""
    dungeon = [[' ' for _ in range(5)] for _ in range(5)]
    width, height = 5, 5
    recursive_divide(dungeon, width, height)
    assert any(cell == '#' for row in dungeon for cell in row)

def test_generate_dungeon():
    """Test the generate_dungeon function with normal inputs."""
    dungeon = generate_dungeon()
    assert isinstance(dungeon, list) and all(isinstance(row, list) for row in dungeon)
    assert len(dungeon[0]) > 0 and len(dungeon) > 0

def test_print_dungeon():
    """Test the print_dungeon function with normal inputs."""
    dungeon = [[' ' for _ in range(5)] for _ in range(5)]
    captured_output = []
    sys.stdout = captured_output
    print_dungeon(dungeon)
    sys.stdout = sys.__stdout__
    assert len(captured_output) > 0

def test_create_room_edge_case():
    """Test the create_room function with edge case inputs (width=1, height=1)."""
    room = create_room(1, 1)
    assert isinstance(room, tuple) and len(room) == 2
    assert all(isinstance(point, tuple) and len(point) == 2 for point in room)

def test_draw_wall_edge_case():
    """Test the draw_wall function with edge case inputs (x1=0, y1=0, x2=0, y2=0)."""
    dungeon = [[' ' for _ in range(5)] for _ in range(5)]
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    draw_wall(dungeon, x1, y1, x2, y2)
    assert dungeon[y1][x1] == '#' and dungeon[y2][x2] == '#'

def test_recursive_divide_edge_case():
    """Test the recursive_divide function with edge case inputs (width=0, height=0)."""
    dungeon = [[' ' for _ in range(5)] for _ in range(5)]
    width, height = 0, 0
    recursive_divide(dungeon, width, height)
    assert all(cell == ' ' for row in dungeon for cell in row)

def test_generate_dungeon_edge_case():
    """Test the generate_dungeon function with edge case inputs (width=1, height=1)."""
    dungeon = generate_dungeon(1, 1)
    assert isinstance(dungeon, list) and all(isinstance(row, list) for row in dungeon)
    assert len(dungeon[0]) == 1 and len(dungeon) == 1

def test_print_dungeon_edge_case():
    """Test the print_dungeon function with edge case inputs (dungeon with one cell)."""
    dungeon = [[' ']]
    captured_output = []
    sys.stdout = captured_output
    print_dungeon(dungeon)
    sys.stdout = sys.__stdout__
    assert len(captured_output) == 1

def test_draw_wall_error_handling():
    """Test the draw_wall function with error handling for invalid inputs."""
    dungeon = [[' ' for _ in range(5)] for _ in range(5)]
    x1, y1 = 0, 0
    x2, y2 = 6, 6
    with pytest.raises(IndexError):
        draw_wall(dungeon, x1, y1, x2, y2)