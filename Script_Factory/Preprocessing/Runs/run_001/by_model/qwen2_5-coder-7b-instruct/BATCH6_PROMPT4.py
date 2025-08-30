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