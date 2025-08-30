import random

def generate_dungeon(width=31, height=21, iterations=5):
    """
    Generates a dungeon map using cellular automata algorithm.

    Args:
        width (int): Width of the dungeon grid.
        height (int): Height of the dungeon grid.
        iterations (int): Number of iterations to run the automata.

    Returns:
        list: 2D list representing the dungeon map with '#' as walls and '.' as floors.
    """
    # Initialize the grid with random walls and floors
    def initialize_grid(width, height):
        return [['.' if random.randint(0, 1) == 1 else '#'
                for _ in range(width)]
               for _ in range(height)]

    def get_neighbors(x, y, grid):
        """Counts the number of wall neighbors around a cell."""
        width = len(grid[0])
        height = len(grid)
        count = 0
        for i in range(max(0, x-1), min(width, x+2)):
            for j in range(max(0, y-1), min(height, y+2)):
                if (i, j) != (x, y) and grid[j][i] == '#':
                    count += 1
        return count

    def apply_rules(grid):
        """Applies the cellular automata rules to evolve the grid."""
        width = len(grid[0])
        height = len(grid)
        new_grid = [['.' for _ in range(width)]
                   for _ in range(height)]

        for y in range(height):
            for x in range(width):
                neighbors = get_neighbors(x, y, grid)

                # Rule: If a wall has 4 or more wall neighbors, it stays a wall
                if grid[y][x] == '#' and neighbors >= 4:
                    new_grid[y][x] = '#'
                # Rule: If a floor has 5 or more wall neighbors, it becomes a wall  
                elif grid[y][x] == '.' and neighbors >= 5:
                    new_grid[y][x] = '#'
        return new_grid

    grid = initialize_grid(width, height)

    for _ in range(iterations):
        grid = apply_rules(grid)

    return grid

def print_dungeon(dungeon_map):
    """Prints the dungeon map to console."""
    for row in dungeon_map:
        print(''.join(row))

if __name__ == "__main__":
    # Generate and display a 31x21 dungeon with 5 iterations
    dungeon = generate_dungeon()
    print_dungeon(dungeon)