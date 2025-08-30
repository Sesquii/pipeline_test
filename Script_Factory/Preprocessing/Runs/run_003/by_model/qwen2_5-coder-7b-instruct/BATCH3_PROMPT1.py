import random

def recursive_division(divided_area):
    """
    Recursively divide a given area into smaller sections to create a dungeon layout.
    
    :param divided_area: A list of lists representing the area to be divided
    :return: A modified version of the area with walls and corridors
    """
    width = len(divided_area[0])
    height = len(divided_area)
    
    if width < 10 or height < 10:
        return
    
    # Choose a random point to split the area (not on an edge)
    horizontal_split = random.randint(2, height - 3)
    vertical_split = random.randint(2, width - 3)
    
    # Add walls along the split
    for i in range(width):
        divided_area[horizontal_split][i] = '#'
    for j in range(height):
        divided_area[j][vertical_split] = '#'
    
    # Clear a path through the walls
    divided_area[horizontal_split][vertical_split] = ' '
    divided_area[horizontal_split + 1][vertical_split] = ' '
    divided_area[horizontal_split - 1][vertical_split] = ' '
    divided_area[horizontal_split][vertical_split + 1] = ' '
    divided_area[horizontal_split][vertical_split - 1] = ' '
    
    # Recursively divide the four sub-areas
    recursive_division([row[:vertical_split] for row in divided_area[:horizontal_split]])
    recursive_division([row[vertical_split:] for row in divided_area[:horizontal_split]])
    recursive_division([row[:vertical_split] for row in divided_area[horizontal_split:]])
    recursive_division([row[vertical_split:] for row in divided_area[horizontal_split:]])

def create_dungeon(width, height):
    """
    Create a basic dungeon layout using the recursive division algorithm.
    
    :param width: Width of the dungeon
    :param height: Height of the dungeon
    :return: A 2D list representing the dungeon map
    """
    # Initialize the dungeon with walls ('#')
    dungeon = [['#' for _ in range(width)] for _ in range(height)]
    
    # Add an entrance and exit
    dungeon[0][1] = 'E'
    dungeon[-1][-2] = 'X'
    
    # Recursively divide the dungeon
    recursive_division(dungeon)
    
    return dungeon

def print_dungeon(dungeon):
    """
    Print the dungeon map to the console.
    
    :param dungeon: A 2D list representing the dungeon map
    """
    for row in dungeon:
        print(''.join(row))

if __name__ == "__main__":
    width = 30
    height = 15
    dungeon = create_dungeon(width, height)
    print_dungeon(dungeon)