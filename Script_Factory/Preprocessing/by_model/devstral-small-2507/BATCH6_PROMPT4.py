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