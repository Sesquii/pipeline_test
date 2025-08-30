# BATCH3_PROMPT7_Granite.py

import random
from PIL import Image

def glitch_image(image_path: str, output_path: str, error_rate: float = 0.1) -> None:
    """
    Glitch an image by randomly introducing pixel errors or artifacts.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the glitched image.
        error_rate (float, optional): Probability of a pixel being affected by the glitch. Defaults to 0.1.
    """
    # Open the image using Pillow's Image module
    img = Image.open(image_path)
    
    width, height = img.size

    # Iterate over each pixel in the image
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))

            # Randomly introduce a glitch with given error rate
            if random.random() < error_rate:
                # Introduce random errors to RGB values
                r += random.randint(-10, 10)
                g += random.randint(-10, 10)
                b += random.randint(-10, 10)

                # Ensure the RGB values stay within valid range (0-255)
                r = max(0, min(255, r))
                g = max(0, min(255, g))
                b = max(0, min(255, b))

            # Set the pixel to the new RGB value
            img.putpixel((x, y), (r, g, b))

    # Save the glitch-ed image
    img.save(output_path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python BATCH3_PROMPT7_Granite.py <input_image> <output_image> <error_rate>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    try:
        error_rate = float(sys.argv[3])
    except ValueError:
        print("Error rate must be a floating point number.")
        sys.exit(1)

    glitch_image(input_path, output_path, error_rate)
    print(f"Glitched image saved to {output_path}")

# ===== GENERATED TESTS =====
# BATCH3_PROMPT7_Granite.py

import random
from PIL import Image
import pytest
from io import BytesIO

def glitch_image(image_path: str, output_path: str, error_rate: float = 0.1) -> None:
    """
    Glitch an image by randomly introducing pixel errors or artifacts.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the glitched image.
        error_rate (float, optional): Probability of a pixel being affected by the glitch. Defaults to 0.1.
    """
    # Open the image using Pillow's Image module
    img = Image.open(image_path)
    
    width, height = img.size

    # Iterate over each pixel in the image
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))

            # Randomly introduce a glitch with given error rate
            if random.random() < error_rate:
                # Introduce random errors to RGB values
                r += random.randint(-10, 10)
                g += random.randint(-10, 10)
                b += random.randint(-10, 10)

                # Ensure the RGB values stay within valid range (0-255)
                r = max(0, min(255, r))
                g = max(0, min(255, g))
                b = max(0, min(255, b))

            # Set the pixel to the new RGB value
            img.putpixel((x, y), (r, g, b))

    # Save the glitch-ed image
    img.save(output_path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python BATCH3_PROMPT7_Granite.py <input_image> <output_image> <error_rate>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    try:
        error_rate = float(sys.argv[3])
    except ValueError:
        print("Error rate must be a floating point number.")
        sys.exit(1)

    glitch_image(input_path, output_path, error_rate)
    print(f"Glitched image saved to {output_path}")

# Test suite for BATCH3_PROMPT7_Granite.py

def test_glitch_image(tmpdir):
    """Test the glitch_image function with a sample image."""
    input_image = tmpdir.join("input.png")
    output_image = tmpdir.join("output.png")

    # Create a sample image
    img = Image.new('RGB', (10, 10), color = (255, 0, 0))
    img.save(input_image)

    glitch_image(str(input_image), str(output_image))

    # Load the output image and check if it has been modified
    output_img = Image.open(output_image)
    assert output_img.size == (10, 10)
    pixels = list(output_img.getdata())
    for pixel in pixels:
        assert all(245 <= c <= 265 for c in pixel), "Pixel values should be within the glitch range"

def test_glitch_image_error_rate(tmpdir):
    """Test the glitch_image function with different error rates."""
    input_image = tmpdir.join("input.png")
    output_image = tmpdir.join("output.png")

    # Create a sample image
    img = Image.new('RGB', (10, 10), color = (255, 0, 0))
    img.save(input_image)

    for error_rate in [0.0, 0.1, 0.5, 1.0]:
        glitch_image(str(input_image), str(output_image), error_rate)
        output_img = Image.open(output_image)
        pixels = list(output_img.getdata())
        if error_rate == 0:
            assert all(c == (255, 0, 0) for c in pixels), "No pixel should be modified"
        else:
            assert any(c != (255, 0, 0) for c in pixels), "At least one pixel should be modified"

def test_glitch_image_invalid_error_rate(tmpdir):
    """Test the glitch_image function with an invalid error rate."""
    input_image = tmpdir.join("input.png")
    output_image = tmpdir.join("output.png")

    # Create a sample image
    img = Image.new('RGB', (10, 10), color = (255, 0, 0))
    img.save(input_image)

    with pytest.raises(ValueError):
        glitch_image(str(input_image), str(output_image), "invalid_error_rate")

def test_glitch_image_missing_input_file(tmpdir):
    """Test the glitch_image function with a missing input file."""
    output_image = tmpdir.join("output.png")

    with pytest.raises(FileNotFoundError):
        glitch_image("nonexistent_image.png", str(output_image))

def test_glitch_image_output_path(tmpdir):
    """Test the glitch_image function with different output paths."""
    input_image = tmpdir.join("input.png")
    img = Image.new('RGB', (10, 10), color = (255, 0, 0))
    img.save(input_image)

    # Test writing to a file
    output_file_path = str(tmpdir.join("output.png"))
    glitch_image(str(input_image), output_file_path)
    assert os.path.exists(output_file_path)

    # Test writing to a directory (should raise an error)
    with pytest.raises(OSError):
        glitch_image(str(input_image), str(tmpdir))

def test_glitch_image_large_error_rate(tmpdir):
    """Test the glitch_image function with a large error rate."""
    input_image = tmpdir.join("input.png")
    output_image = tmpdir.join("output.png")

    # Create a sample image
    img = Image.new('RGB', (10, 10), color = (255, 0, 0))
    img.save(input_image)

    glitch_image(str(input_image), str(output_image), error_rate=1.0)
    output_img = Image.open(output_image)
    pixels = list(output_img.getdata())
    assert all(c != (255, 0, 0) for c in pixels), "All pixels should be modified"

def test_glitch_image_small_error_rate(tmpdir):
    """Test the glitch_image function with a small error rate."""
    input_image = tmpdir.join("input.png")
    output_image = tmpdir.join("output.png")

    # Create a sample image
    img = Image.new('RGB', (10, 10), color = (255, 0, 0))
    img.save(input_image)

    glitch_image(str(input_image), str(output_image), error_rate=0.0)
    output_img = Image.open(output_image)
    pixels = list(output_img.getdata())
    assert all(c == (255, 0, 0) for c in pixels), "No pixel should be modified"
