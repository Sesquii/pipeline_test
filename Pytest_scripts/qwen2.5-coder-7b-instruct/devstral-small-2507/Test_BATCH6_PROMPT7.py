from PIL import Image
import random

def glitchy_image_compressor(input_file_path):
    """
    Compresses an image by randomly corrupting pixel RGB values to 0.

    Args:
        input_file_path (str): Path to the input JPG image file.
    """

    # Open the image file
    with Image.open(input_file_path) as img:
        # Convert to RGB mode if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Get image dimensions
        width, height = img.size

        # Get pixel data
        pixels = list(img.getdata())

        # Determine how many pixels to corrupt (10% of total pixels)
        num_pixels_to_corrupt = int(len(pixels) * 0.1)

        for _ in range(num_pixels_to_corrupt):
            # Select a random pixel
            pixel_index = random.randint(0, len(pixels) - 1)

            # Randomly choose which color channel to set to 0 (Red, Green, or Blue)
            corrupt_channel = random.randint(0, 2)

            # Create a new pixel tuple with one channel set to 0
            new_pixel = list(pixels[pixel_index])
            new_pixel[corrupt_channel] = 0

            # Update the pixel data
            pixels[pixel_index] = tuple(new_pixel)

        # Create a new image from the modified pixel data
        corrupted_img = Image.new('RGB', (width, height))
        corrupted_img.putdata(pixels)

        # Generate output filename
        output_file_path = f"{input_file_path}_corrupt.jpg"

        # Save the corrupted image
        corrupted_img.save(output_file_path)
        print(f"Glitchy compressed image saved to {output_file_path}")

if __name__ == "__main__":
    # Example usage: Replace 'example.jpg' with your actual image file path
    glitchy_image_compressor('example.jpg')

# ===== GENERATED TESTS =====
```python
from PIL import Image
import random
import pytest
from io import BytesIO

def glitchy_image_compressor(input_file_path):
    """
    Compresses an image by randomly corrupting pixel RGB values to 0.

    Args:
        input_file_path (str): Path to the input JPG image file.
    """

    # Open the image file
    with Image.open(input_file_path) as img:
        # Convert to RGB mode if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Get image dimensions
        width, height = img.size

        # Get pixel data
        pixels = list(img.getdata())

        # Determine how many pixels to corrupt (10% of total pixels)
        num_pixels_to_corrupt = int(len(pixels) * 0.1)

        for _ in range(num_pixels_to_corrupt):
            # Select a random pixel
            pixel_index = random.randint(0, len(pixels) - 1)

            # Randomly choose which color channel to set to 0 (Red, Green, or Blue)
            corrupt_channel = random.randint(0, 2)

            # Create a new pixel tuple with one channel set to 0
            new_pixel = list(pixels[pixel_index])
            new_pixel[corrupt_channel] = 0

            # Update the pixel data
            pixels[pixel_index] = tuple(new_pixel)

        # Create a new image from the modified pixel data
        corrupted_img = Image.new('RGB', (width, height))
        corrupted_img.putdata(pixels)

        # Generate output filename
        output_file_path = f"{input_file_path}_corrupt.jpg"

        # Save the corrupted image
        corrupted_img.save(output_file_path)
        print(f"Glitchy compressed image saved to {output_file_path}")

# Test suite for glitchy_image_compressor function

def test_glitchy_image_compressor(tmpdir):
    """
    Tests the glitchy_image_compressor function with a temporary image file.
    """

    # Create a temporary image file
    input_image = Image.new('RGB', (100, 100), color='red')
    input_file_path = str(tmpdir.join("test.jpg"))
    input_image.save(input_file_path)

    # Call the glitchy_image_compressor function
    glitchy_image_compressor(input_file_path)

    # Check if the output file exists
    assert tmpdir.join(f"test_corrupt.jpg").exists()

def test_glitchy_image_compressor_with_non_rgb_mode(tmpdir):
    """
    Tests the glitchy_image_compressor function with a non-RGB image mode.
    """

    # Create a temporary image file in CMYK mode
    input_image = Image.new('CMYK', (100, 100), color='red')
    input_file_path = str(tmpdir.join("test_cmyk.jpg"))
    input_image.save(input_file_path)

    # Call the glitchy_image_compressor function
    glitchy_image_compressor(input_file_path)

    # Check if the output file exists and is in RGB mode
    output_image = Image.open(str(tmpdir.join(f"test_cmyk_corrupt.jpg")))
    assert output_image.mode == 'RGB'

def test_glitchy_image_compressor_with_empty_input_file(tmpdir):
    """
    Tests the glitchy_image_compressor function with an empty input file.
    """

    # Create a temporary empty image file
    input_file_path = str(tmpdir.join("empty.jpg"))
    open(input_file_path, 'w').close()

    # Call the glitchy_image_compressor function and expect it to raise an exception
    with pytest.raises(IOError):
        glitchy_image_compressor(input_file_path)

def test_glitchy_image_compressor_with_non_jpg_extension(tmpdir):
    """
    Tests the glitchy_image_compressor function with a non-JPG file extension.
    """

    # Create a temporary image file with a non-JPG extension
    input_image = Image.new('RGB', (100, 100), color='red')
    input_file_path = str(tmpdir.join("test.png"))
    input_image.save(input_file_path)

    # Call the glitchy_image_compressor function and expect it to raise an exception
    with pytest.raises(IOError):
        glitchy_image_compressor(input_file_path)
```