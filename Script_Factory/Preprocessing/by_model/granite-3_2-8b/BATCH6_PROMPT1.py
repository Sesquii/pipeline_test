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