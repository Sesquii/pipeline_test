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

# ===== GENERATED TESTS =====
```python
from PIL import Image
import random
import pytest

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

# Test cases
def test_dither_image():
    """Test the dither_image function."""
    input_image = Image.new('RGB', (2, 2), color=(100, 150, 200))
    palette = [(0, 0, 0), (255, 255, 255)]
    dithered_image = dither_image(input_image, palette)
    for i in range(2):
        for j in range(2):
            assert dithered_image.getpixel((i, j)) in palette

def test_apply_swaps():
    """Test the apply_swaps function."""
    input_image = Image.new('RGB', (2, 2), color=(100, 150, 200))
    palette = [(0, 0, 0), (255, 255, 255)]
    apply_swaps(input_image, palette)
    for i in range(2):
        for j in range(2):
            assert input_image.getpixel((i, j)) in palette

def test_main():
    """Test the main function."""
    # This is a bit tricky to test directly since it involves file operations.
    # We can mock the Image.open and Image.save methods to check if they are called.
    with patch('PIL.Image.open') as mock_open:
        with patch('PIL.Image.save') as mock_save:
            main()
            mock_open.assert_called_once_with('input.png')
            mock_save.assert_called_once()

# Fixtures
@pytest.fixture
def input_image():
    """Fixture to create a test image."""
    return Image.new('RGB', (2, 2), color=(100, 150, 200))

@pytest.fixture
def palette():
    """Fixture to provide a test palette."""
    return [(0, 0, 0), (255, 255, 255)]

# Parametrization
@pytest.mark.parametrize("palette", [
    [(0, 0, 0), (255, 255, 255)],
    [(128, 128, 128), (255, 0, 0)]
])
def test_dither_image_with_palette(input_image, palette):
    """Test the dither_image function with different palettes."""
    dithered_image = dither_image(input_image, palette)
    for i in range(2):
        for j in range(2):
            assert dithered_image.getpixel((i, j)) in palette

@pytest.mark.parametrize("swap_probability", [0.0, 1.0])
def test_apply_swaps_with_probability(input_image, palette, swap_probability):
    """Test the apply_swaps function with different swap probabilities."""
    input_image.putpixel((0, 0), (255, 0, 0))
    input_image.putpixel((1, 1), (0, 255, 0))
    apply_swaps(input_image, palette, swap_probability)
    for i in range(2):
        for j in range(2):
            assert input_image.getpixel((i, j)) in palette
```