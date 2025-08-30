import sys

def generate_dungeon(x1, y1, x2, y2):
    # Initialize a grid with walls (0) and open spaces (1)
    grid = [[0]*(x2 - x1 + 1) for _ in range(y2 - y1 + 1)]
    
    # Fill the current area with open spaces
    for i in range(y2 - y1 + 1):
        for j in range(x2 - x1 + 1):
            grid[i][j] = 1
    
    mid_x = (x1 + x2) // 2
    mid_y = (y1 + y2) // 2

    # Generate left and right quadrants
    generate_dungeon(x1, y1, mid_x - 1, y2)
    generate_dungeon(mid_x, y1, x2, y2)

    # Generate top and bottom quadrants
    generate_dungeon(x1, y1, mid_y - 1, y2)
    generate_dungeon(x1, y2, mid_y + 1, x2)

    return grid

def main():
    if len(sys.argv) < 2:
        print("Usage: python BATCH3_PROMPT1_{{model_name}}.py")
        sys.exit(1)
    
    # Create a dungeon of size 10x10
    dungeon = generate_dungeon(0, 0, 9, 9)
    for row in dungeon:
        print(''.join(['#' if cell == 0 else 'O' for cell in row]))

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Original script remains unchanged

def test_generate_dungeon():
    """Test the generate_dungeon function with various inputs."""
    
    # Test case 1: Basic 2x2 dungeon
    grid = generate_dungeon(0, 0, 1, 1)
    assert grid == [[1, 1], [1, 1]], "Failed test case 1"
    
    # Test case 2: Larger 3x3 dungeon
    grid = generate_dungeon(0, 0, 2, 2)
    expected_grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert grid == expected_grid, "Failed test case 2"
    
    # Test case 3: Negative coordinates
    with pytest.raises(ValueError):
        generate_dungeon(-1, -1, 0, 0)
    
    # Test case 4: Non-integer inputs
    with pytest.raises(TypeError):
        generate_dungeon(0.5, 0.5, 1.5, 1.5)

def test_main(capsys):
    """Test the main function with various inputs."""
    
    # Mock sys.argv for testing
    sys.argv = ['script.py']
    
    # Capture output
    capsys.readouterr()
    main()
    
    # Check if the output is as expected
    captured = capsys.readouterr().out
    assert 'O' in captured, "Failed test case: Output does not contain open spaces"
    assert '#' in captured, "Failed test case: Output does not contain walls"

# Add more tests as needed
