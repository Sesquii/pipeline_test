from PIL import Image
import random

def dither_image(input_path):
    # Open image file
    img = Image.open(input_path)

    # Convert image to RGB (in case it's not)
    img = img.convert("RGB")

    # Get image size
    width, height = img.size

    # Reduce color palette to 3 colors using a simple quantization method
    def reduce_palette(image):
        colors = image.getcolors(image.size[0] * image.size[1])
        total_pixels = sum([count for count, color in colors[:3]])

        reduced_img = Image.new("RGB", (width, height))
        pixels = reduced_img.load()

        # Sort colors by quantity and choose top 3
        colors.sort(key=lambda x: x[0], reverse=True)[:3]

        for count, color in colors:
            for _ in range(count):
                x, y = random.randint(0, width - 1), random.randint(0, height - 1)
                pixels[x, y] = color

        return reduced_img

    # Apply reduction and dithering
    dithered_img = reduce_palette(img)

    # Save the dithered image with a new filename
    output_path = f"{input_path.split('/')[-1].rsplit('.', 1)[0]}_dithered.png"
    dithered_img.save(output_path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python glitchy_compressor.py <path_to_image>")
    else:
        input_file = sys.argv[1]
        dither_image(input_file)
        print(f"Dithered image saved as {input_file.rsplit('.', 1)[0]}_dithered.png")

# ===== GENERATED TESTS =====
from PIL import Image
import random
import pytest

def dither_image(input_path):
    # Open image file
    img = Image.open(input_path)

    # Convert image to RGB (in case it's not)
    img = img.convert("RGB")

    # Get image size
    width, height = img.size

    # Reduce color palette to 3 colors using a simple quantization method
    def reduce_palette(image):
        colors = image.getcolors(image.size[0] * image.size[1])
        total_pixels = sum([count for count, color in colors[:3]])

        reduced_img = Image.new("RGB", (width, height))
        pixels = reduced_img.load()

        # Sort colors by quantity and choose top 3
        colors.sort(key=lambda x: x[0], reverse=True)[:3]

        for count, color in colors:
            for _ in range(count):
                x, y = random.randint(0, width - 1), random.randint(0, height - 1)
                pixels[x, y] = color

        return reduced_img

    # Apply reduction and dithering
    dithered_img = reduce_palette(img)

    # Save the dithered image with a new filename
    output_path = f"{input_path.split('/')[-1].rsplit('.', 1)[0]}_dithered.png"
    dithered_img.save(output_path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python glitchy_compressor.py <path_to_image>")
    else:
        input_file = sys.argv[1]
        dither_image(input_file)
        print(f"Dithered image saved as {input_file.rsplit('.', 1)[0]}_dithered.png")

# Test suite for the dither_image function

@pytest.fixture
def test_image(tmp_path):
    # Create a temporary test image with random pixels
    width, height = 50, 50
    img = Image.new("RGB", (width, height))
    pixels = img.load()
    for x in range(width):
        for y in range(height):
            pixels[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    test_path = tmp_path / "test_image.png"
    img.save(test_path)
    return test_path

def test_dither_image(test_image):
    """Test the dither_image function with a temporary image."""
    output_path = f"{test_image.rsplit('.', 1)[0]}_dithered.png"
    try:
        dither_image(str(test_image))
        assert Path(output_path).exists()
    finally:
        # Clean up the generated file
        if Path(output_path).exists():
            Path(output_path).unlink()

def test_dither_image_invalid_input():
    """Test the dither_image function with an invalid input."""
    with pytest.raises(FileNotFoundError):
        dither_image("nonexistent_file.png")

# Additional tests can be added here following similar patterns
