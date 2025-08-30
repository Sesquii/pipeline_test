import random

class BSPNode:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.left = None
        self.right = None
        self.split = False

    def split(self):
        if not self.split:
            self.split = True
            if random.choice([True, False]):
                # Split horizontally
                sx = self.x + random.randint(1, self.width - 2)
                self.left = BSPNode(self.x, self.y, sx - self.x, self.height)
                self.right = BSPNode(sx, self.y, self.x + self.width - sx, self.height)
            else:
                # Split vertically
                sy = self.y + random.randint(1, self.height - 2) 
                self.left = BSPNode(self.x, self.y, self.width, sy - self.y)
                self.right = BSPNode(self.x, sy, self.width, self.y + self.height - sy)

    def draw(self, grid):
        for x in range(self.x, self.x + self.width):
            for y in range(self.y, self.y + self.height):
                if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                    grid[y][x] = '#'

        if self.left:
            # Connect rooms with ~
            if self.left.y == self.right.y:  # Horizontal split
                cx = (self.left.x + self.right.x) // 2
                cy = random.randint(self.left.y, min(self.left.y + self.left.height - 1, HEIGHT - 1))
                grid[cy][cx] = '~'
            else:  # Vertical split  
                cx = random.randint(self.left.x, min(self.left.x + self.left.width - 1, WIDTH - 1))
                cy = (self.left.y + self.right.y) // 2
                grid[cy][cx] = '~'

    def generate_dungeon(self):
        if self.width > MIN_SIZE and self.height > MIN_SIZE:
            self.split()
            if self.left:
                self.left.generate_dungeon()
            if self.right:
                self.right.generate_dungeon()

def print_grid(grid):
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    WIDTH = 40
    HEIGHT = 20
    MIN_SIZE = 5

    # Initialize empty grid with spaces
    grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Create root node and generate dungeon
    root = BSPNode(0, 0, WIDTH, HEIGHT)
    root.generate_dungeon()
    root.draw(grid)

    print_grid(grid)