import random

# Constants for ASCII characters
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', '=', '-', '.', ' ']

def draw_shape(x, y, size, depth, canvas):
    if depth == 0 or size < 1:
        return

    # Draw the current shape
    for i in range(size):
        for j in range(size):
            char_index = int((i * size + j) / (size * size) * (len(ASCII_CHARS) - 1))
            canvas[y + i][x + j] = ASCII_CHARS[char_index]

    # Recursively draw smaller shapes around the current one
    if depth > 1:
        new_size = max(1, int(size * 0.7))
        new_depth = depth - 1

        # Draw shapes in a cross pattern around the current shape
        directions = [
            (x - new_size - 1, y),     # left
            (x + size + 1, y),         # right
            (x, y - new_size - 1),     # up
            (x, y + size + 1)          # down
        ]

        for dx, dy in directions:
            if dx >= 0 and dy >= 0 and dx + new_size < len(canvas[0]) and dy + new_size < len(canvas):
                draw_shape(dx, dy, new_size, new_depth, canvas)

def create_canvas(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]

def print_canvas(canvas):
    for row in canvas:
        print(''.join(row))

def digital_artist(width=40, height=20, initial_size=15, max_depth=3):
    canvas = create_canvas(width, height)
    start_x = (width - initial_size) // 2
    start_y = (height - initial_size) // 2

    draw_shape(start_x, start_y, initial_size, max_depth, canvas)
    print_canvas(canvas)

if __name__ == "__main__":
    digital_artist()