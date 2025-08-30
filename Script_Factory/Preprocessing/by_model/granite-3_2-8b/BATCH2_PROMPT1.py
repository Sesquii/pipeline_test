import random

class DungeonGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate(self):
        dungeon = [['#'] * (2 * w + 1) for _ in range(2 * h + 1)]  # Initialize a larger grid with walls

        def add_wall(x, y):
            if 0 < x < len(dungeon[0]) - 1 and 0 < y < len(dungeon) - 1:
                dungeon[y][x] = '#'  # Wall

        def carve_passage(min_x, max_x, min_y, max_y):
            if random.randint(0, 100) > 95:  # Random chance to carve a passage
                x, y = random.randint(min_x, max_x), random.randint(min_y, max_y)
                add_wall(x, y)

                if random.choice([True, False]):
                    self.carve_passage(min_x, x - 1, min_y, y)
                    self.carve_passage(x + 1, max_x, min_y, y)
                else:
                    self.carve_passage(min_x, x, min_y, y - 1)
                    self.carve_passage(min_x, x, y + 1, max_y)

        for _ in range(int((self.width / 2) * self.height)):
            carve_passage(0, self.width, 0, self.height)

        # Remove outer walls
        dungeon = [row for row in zip(*dungeon) if row[0] != '#' or row[-1] != '#']
        dungeon = [row for row in zip(*dungeon) if row[0] != '#' or row[-1] != '#']

        return dungeon


def print_dungeon(dungeon):
    for row in dungeon:
        print(''.join(row))


if __name__ == "__main__":
    generator = DungeonGenerator(30, 15)
    dungeon = generator.generate()
    print_dungeon(dungeon)