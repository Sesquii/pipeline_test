import random

class ProceduralDungeonGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [['#' for _ in range(width)] for _ in range(height)]

    def generate(self):
        self.recursive_division(0, 0, self.width, self.height)

    def recursive_division(self, x, y, w, h):
        if w < 2 or h < 2:
            return

        # Decide whether to divide horizontally or vertically
        if w > h and w > 1 and random.random() > 0.5:
            self.divide_horizontally(x, y, w, h)
        else:
            self.divide_vertically(x, y, w, h)

    def divide_horizontally(self, x, y, w, h):
        split_at = random.randint(1, h - 2)
        path_y = y + split_at

        for i in range(w):
            if random.random() > 0.2:
                self.map[path_y][x + i] = '.'

        self.recursive_division(x, y, w, split_at)
        self.recursive_division(x, y + split_at + 1, w, h - split_at - 1)

    def divide_vertically(self, x, y, w, h):
        split_at = random.randint(1, w - 2)
        path_x = x + split_at

        for i in range(h):
            if random.random() > 0.2:
                self.map[y + i][path_x] = '.'

        self.recursive_division(x, y, split_at, h)
        self.recursive_division(x + split_at + 1, y, w - split_at - 1, h)

    def print_map(self):
        for row in self.map:
            print(''.join(row))

if __name__ == "__main__":
    width = 30
    height = 20
    generator = ProceduralDungeonGenerator(width, height)
    generator.generate()
    generator.print_map()