```python
from PIL import Image
import random

def dither_image(image, palette):
    """Reduces image color palette to a specified set of colors."""
    width, height = image.size
    new_image = Image.new('RGB', (width, height))
    for i in range(width):
        for j in range(height):
            original_color = image.getpixel((i, j))
            selected_color = random.choice(palette)
            new_image.putpixel((i, j), selected_color)
    return new_image

def apply_swaps(image, palette):
    """Randomly swaps pixels with different colors in the reduced palette."""
    width, height = image.size
    for i in range(width):
        for j in range(height):
            current_color = image.getpixel((i, j))
            if random.random() < 0.5:
                x, y = random.randint(0, width - 1), random.randint(0, height - 1)
                other_color = image.getpixel((x, y))
                if current_color != other_color:
                    # Swap the colors
                    new_color = other_color
                    image.putpixel((i, j), new_color)
                    image.putpixel((x, y), current_color)

def main():
    input_path = 'input.png'
    output_path = f"{input_path}_dithered.png"
    image = Image.open(input_path)
    # Reduce color palette to 2 colors (black and white)
    palette = [(0, 0, 0), (255, 255, 255)]
    dithered_image = dither_image(image, palette)
    apply_swaps(dithered_image, palette)
    dithered_image.save(output_path)

if __name__ == "__main__":
    main()