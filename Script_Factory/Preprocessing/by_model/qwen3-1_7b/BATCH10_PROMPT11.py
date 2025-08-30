```python
def draw_pattern(size):
    """Draws an abstract pattern using recursion."""
    if size == 0:
        return
    # Draw the top part of the pattern
    for i in range(size):
        print(' ' * (size - i - 1) + '*' * (2*i + 1))
    # Recursively call to draw the next level
    draw_pattern(size-1)

if __name__ == "__main__":
    draw_pattern(5)