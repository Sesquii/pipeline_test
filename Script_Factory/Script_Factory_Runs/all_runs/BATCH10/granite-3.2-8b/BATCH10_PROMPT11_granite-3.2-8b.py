import random

def draw_shape(size, char='#', depth=0):
    """Recursive function to draw an abstract shape using ASCII characters."""
    if depth > 5:  # Limit recursion depth for stability
        return

    max_width = size * (2 ** depth) - 1
    spaces = ' ' * ((max_width + size - 1) // 2)
    lines = [spaces + char * width + spaces for width in range(size, -1, -2)]

    # Print the shape
    for line in lines:
        print(line.center(max_width))

    # Recursively call with increased depth and size
    draw_shape(size * 2, char, depth + 1)
    if depth > 0:
        draw_shape(size * 2, char, depth - 1)

def main():
    """Entry point of the program."""
    size = int(input("Enter the starting size of the shape: "))
    char = input("Choose a character to use (default '#' is recommended): ") or '#'

    print(f"\nDrawing an abstract shape with size {size} and character '{char}'...")
    draw_shape(size, char)

if __name__ == "__main__":
    main()