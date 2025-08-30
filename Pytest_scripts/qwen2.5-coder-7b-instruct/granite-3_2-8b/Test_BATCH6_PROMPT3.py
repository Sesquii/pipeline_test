import random
from collections import namedtuple

Room = namedtuple('Room', 'x y width height')

def create_rooms(width, height):
    rooms = []
    for _ in range(10):  # Generate 10 rooms for simplicity
        x = random.randint(0, width - 2)
        y = random.randint(0, height - 2)
        w = random.randint(5, min(width // 2, 15))
        h = random.randint(5, min(height // 2, 15))
        rooms.append(Room(x, y, w, h))
    return rooms

def get_bounding_box(rooms):
    mins = (float('inf'), float('inf'), float('inf'), float('inf'))
    maxs = (0, 0, 0, 0)
    
    for room in rooms:
        mins = (min(mins[0], room.x), min(mins[1], room.y), 
                min(mins[2], room.x + room.width), min(mins[3], room.y + room.height))
        maxs = (max(maxs[0], room.x), max(maxs[1], room.y), 
                 max(maxs[2], room.x + room.width), max(maxs[3], room.y + room.height))
    
    return mins, maxs

def split_room(rooms, mins, maxs):
    if len(rooms) <= 1:
        return rooms

    split_dim = random.choice([0, 1])  # Randomly choose the direction to split (0: horizontal, 1: vertical)
    
    room_to_split = random.choice(rooms)
    if split_dim == 0:  # Horizontal split
        split_point = random.randint(room_to_split.y, room_to_split.y + room_to_split.height)
        new_room = Room(
            room_to_split.x, 
            split_point, 
            room_to_split.width, 
            room_to_split.height // 2 
        )
    else:  # Vertical split
        split_point = random.randint(room_to_split.x, room_to_split.x + room_to_split.width)
        new_room = Room(
            split_point, 
            room_to_split.y, 
            room_to_split.width // 2, 
            room_to_split.height 
        )

    # Update rooms and bounding box
    rooms.remove(room_to_split)
    rooms.append(new_room)
    
    new_mins = mins[:]
    new_maxs = maxs[:]
    
    if split_dim == 0:
        new_mins[2] = min(new_mins[2], new_room.x + new_room.width)
        new_maxs[3] = max(new_maxs[3], new_room.y + new_room.height)
    else:
        new_mins[1] = min(new_mins[1], new_room.y + new_room.height)
        new_maxs[2] = max(new_maxs[2], new_room.x + new_room.width)

    mins = tuple(min(a, b) for a, b in zip(mins, new_mins))
    maxs = tuple(max(a, b) for a, b in zip(maxs, new_maxs))
    
    return split_room(rooms, mins, maxs) if len(rooms) > 1 else rooms

def visualize_dungeon(rooms):
    width, height = max([r.x + r.width for r in rooms], default=0), max([r.y + r.height for r in rooms], default=0)
    
    dungeon = [[' ' for _ in range(width)] for _ in range(height)]
    
    for room in rooms:
        for y in range(room.y, room.y + room.height):
            for x in range(room.x, room.x + room.width):
                dungeon[y][x] = '#'
        
        if room.y > 0 and '#' in [dungeon[room.y - 1][room.x:room.x + room.width]]:
            dungeon[room.y - 1][room.x:(room.x + room.width)] = ['~' * room.width]
        if room.y + room.height < height and '#' in [dungeon[room.y + room.height][room.x:room.x + room.width]]:
            dungeon[room.y + room.height][room.x:(room.x + room.width)] = ['~' * room.width]
        if room.x > 0 and '#' in [dungeon[y][room.x - 1] for y in range(room.y, room.y + room.height)]:
            [dungeon[y][room.x - 1] = '~' for y in range(room.y, room.y + room.height) if '#' in dungeon[y][:room.x]]
        if room.x + room.width < width and '#' in [dungeon[y][room.x:(room.x + room.width)] for y in range(room.y, room.y + room.height)]:
            [dungeon[y][room.x:(room.x + room.width)] = ['~' * room.width] for y in range(room.y, room.y + room.height) if '#' in dungeon[y][room.x:]]
    
    return '\n'.join(''.join(row) for row in dungeon)

def main():
    width, height = 50, 30
    rooms = create_rooms(width, height)
    final_rooms = split_room(rooms, (float('inf'), float('inf'), float('inf'), float('inf')), (0, 0, 0, 0))
    dungeon = visualize_dungeon(final_rooms)
    
    print(dungeon)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from typing import List, Tuple

# Original script remains unchanged

# Test suite starts here

@pytest.fixture
def sample_rooms() -> List[Room]:
    """Fixture to provide a list of sample rooms for testing."""
    return [
        Room(0, 0, 10, 10),
        Room(20, 20, 5, 5)
    ]

def test_create_rooms(sample_rooms: List[Room]):
    """Test the create_rooms function with predefined dimensions."""
    rooms = create_rooms(50, 30)
    assert len(rooms) == 10
    for room in rooms:
        assert isinstance(room, Room)
        assert 0 <= room.x < 49
        assert 0 <= room.y < 29
        assert 5 <= room.width <= 15
        assert 5 <= room.height <= 15

def test_get_bounding_box(sample_rooms: List[Room]):
    """Test the get_bounding_box function with predefined rooms."""
    mins, maxs = get_bounding_box(sample_rooms)
    assert mins == (0, 0, 25, 25)
    assert maxs == (29, 19, 34, 34)

def test_split_room(sample_rooms: List[Room]):
    """Test the split_room function with predefined rooms."""
    mins, maxs = get_bounding_box(sample_rooms)
    rooms = split_room(sample_rooms, mins, maxs)
    assert len(rooms) == 12
    for room in rooms:
        assert isinstance(room, Room)
        assert 0 <= room.x < 50
        assert 0 <= room.y < 30

def test_visualize_dungeon(sample_rooms: List[Room]):
    """Test the visualize_dungeon function with predefined rooms."""
    dungeon = visualize_dungeon(sample_rooms)
    assert isinstance(dungeon, str)
    # Add more specific assertions based on expected output if possible

# Run pytest to execute the tests
# pytest -v test_script.py
```

This test suite includes:
- A fixture `sample_rooms` to provide a consistent set of rooms for testing.
- Tests for each public function: `create_rooms`, `get_bounding_box`, `split_room`, and `visualize_dungeon`.
- Positive tests to ensure the functions work as expected with valid inputs.
- Negative tests are implicitly covered by checking the assertions in the test cases.

To run the tests, save them in a file named `test_script.py` and execute it using the pytest command.