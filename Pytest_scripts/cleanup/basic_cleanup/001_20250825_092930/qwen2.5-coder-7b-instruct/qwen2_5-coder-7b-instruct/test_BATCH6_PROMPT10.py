# Import necessary libraries
from PIL import Image, ImageDraw
import random

def dither_image(input_path):
    """
    Dithers an image by reducing its color palette to 2-3 colors and then swapping pixels.
    
    Args:
    input_path (str): The path to the PNG file to be dithered.
    
    Returns:
    None: Saves the dithered image as <input_filename>_dithered.png
    """
    # Open the image
    img = Image.open(input_path)
    
    # Convert the image to RGB mode
    img = img.convert("RGB")
    
    # Reduce color palette to 2-3 colors
    reduced_colors = []
    pixels = list(img.getdata())
    unique_pixels = set(pixels)
    
    for pixel in unique_pixels:
        if len(reduced_colors) < 2 and random.choice([True, False]):
            reduced_colors.append(pixel)
        elif len(reduced_colors) == 2 and not any(all(c1 == c2 for c1, c2 in zip(pixel, color)) for color in reduced_colors):
            if random.choice([True, False]):
                reduced_colors.append(pixel)
    
    # Create a new image with the reduced colors
    dithered_img = Image.new("RGB", img.size)
    draw = ImageDraw.Draw(dithered_img)
    
    for x in range(img.width):
        for y in range(img.height):
            pixel = pixels[y * img.width + x]
            closest_color = min(reduced_colors, key=lambda color: sum((c1 - c2) ** 2 for c1, c2 in zip(pixel, color)))
            draw.point((x, y), fill=closest_color)
    
    # Randomly swap pixels with a different color from the reduced palette
    for _ in range(10 * img.width * img.height):  # Number of swaps
        x1, y1 = random.randint(0, img.width - 1), random.randint(0, img.height - 1)
        pixel1 = pixels[y1 * img.width + x1]
        if pixel1 in reduced_colors:
            color_options = [color for color in reduced_colors if color != pixel1]
            new_color = random.choice(color_options) if color_options else pixel1
            pixels[y1 * img.width + x1] = new_color
    
    # Save the dithered image
    output_path = f"{input_path.split('.')[0]}_dithered.png"
    dithered_img.putdata(pixels)
    dithered_img.save(output_path)

# Entry point of the script
if __name__ == "__main__":
    input_path = "path_to_your_image.png"  # Replace with your image path
    dither_image(input_path)

This Python program uses the `Pillow` library to open and manipulate an image. It reduces the color palette of the image to 2-3 colors by randomly selecting unique pixels from the original image. Then, it swaps each pixel with a different color from the reduced palette. The dithered image is saved as `<input_filename>_dithered.png`.

# ===== GENERATED TESTS =====
# Import necessary libraries for testing
import pytest
from PIL import Image
import os

# Test fixture to create a temporary PNG file for testing
@pytest.fixture(scope="module")
def temp_png_file(tmpdir):
    # Create a temporary PNG image
    img = Image.new("RGB", (10, 10), color=(255, 0, 0))
    img_path = os.path.join(tmpdir, "test_image.png")
    img.save(img_path)
    
    yield img_path
    
    # Clean up the temporary file after tests
    os.remove(img_path)

# Test function for dither_image with a valid input path
def test_dither_image_valid_input(temp_png_file):
    """
    Tests the dither_image function with a valid input path.
    """
    dither_image(temp_png_file)
    
    # Check if the output file exists
    output_path = f"{temp_png_file.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the output file after test
    os.remove(output_path)

# Test function for dither_image with an invalid input path
def test_dither_image_invalid_input():
    """
    Tests the dither_image function with an invalid input path.
    """
    with pytest.raises(FileNotFoundError):
        dither_image("non_existent_file.png")

# Test function for dither_image with a non-PNG file
def test_dither_image_non_png_file(temp_png_file):
    """
    Tests the dither_image function with a non-PNG file.
    """
    # Convert the PNG image to JPEG format
    img = Image.open(temp_png_file)
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_image.jpg")
    img.save(img_path, "JPEG")
    
    with pytest.raises(ValueError):
        dither_image(img_path)
    
    # Clean up the temporary JPEG file after test
    os.remove(img_path)

# Test function for dither_image with a very small image
def test_dither_image_small_image(temp_png_file):
    """
    Tests the dither_image function with a very small image.
    """
    img = Image.new("RGB", (2, 2), color=(0, 255, 0))
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_small_image.png")
    img.save(img_path)
    
    dither_image(img_path)
    
    # Check if the output file exists
    output_path = f"{img_path.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the temporary file and output file after test
    os.remove(img_path)
    os.remove(output_path)

# Test function for dither_image with a very large image
def test_dither_image_large_image(temp_png_file):
    """
    Tests the dither_image function with a very large image.
    """
    img = Image.new("RGB", (1000, 1000), color=(0, 0, 255))
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_large_image.png")
    img.save(img_path)
    
    dither_image(img_path)
    
    # Check if the output file exists
    output_path = f"{img_path.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the temporary file and output file after test
    os.remove(img_path)
    os.remove(output_path)

# Test function for dither_image with a color palette of 2 colors
def test_dither_image_two_colors(temp_png_file):
    """
    Tests the dither_image function with a color palette of 2 colors.
    """
    img = Image.new("RGB", (10, 10), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 5, 5), fill=(0, 0, 0))
    
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_two_colors.png")
    img.save(img_path)
    
    dither_image(img_path)
    
    # Check if the output file exists
    output_path = f"{img_path.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the temporary file and output file after test
    os.remove(img_path)
    os.remove(output_path)

# Test function for dither_image with a color palette of 3 colors
def test_dither_image_three_colors(temp_png_file):
    """
    Tests the dither_image function with a color palette of 3 colors.
    """
    img = Image.new("RGB", (10, 10), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 3, 3), fill=(0, 0, 0))
    draw.rectangle((4, 4, 7, 7), fill=(128, 128, 128))
    
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_three_colors.png")
    img.save(img_path)
    
    dither_image(img_path)
    
    # Check if the output file exists
    output_path = f"{img_path.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the temporary file and output file after test
    os.remove(img_path)
    os.remove(output_path)

# Test function for dither_image with a color palette of 4 colors
def test_dither_image_four_colors(temp_png_file):
    """
    Tests the dither_image function with a color palette of 4 colors.
    """
    img = Image.new("RGB", (10, 10), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 3, 3), fill=(0, 0, 0))
    draw.rectangle((4, 4, 7, 7), fill=(128, 128, 128))
    draw.rectangle((8, 8, 9, 9), fill=(255, 0, 0))
    
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_four_colors.png")
    img.save(img_path)
    
    dither_image(img_path)
    
    # Check if the output file exists
    output_path = f"{img_path.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the temporary file and output file after test
    os.remove(img_path)
    os.remove(output_path)

# Test function for dither_image with a color palette of 5 colors
def test_dither_image_five_colors(temp_png_file):
    """
    Tests the dither_image function with a color palette of 5 colors.
    """
    img = Image.new("RGB", (10, 10), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 3, 3), fill=(0, 0, 0))
    draw.rectangle((4, 4, 7, 7), fill=(128, 128, 128))
    draw.rectangle((8, 8, 9, 9), fill=(255, 0, 0))
    draw.rectangle((1, 1, 4, 4), fill=(0, 255, 0))
    
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_five_colors.png")
    img.save(img_path)
    
    dither_image(img_path)
    
    # Check if the output file exists
    output_path = f"{img_path.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the temporary file and output file after test
    os.remove(img_path)
    os.remove(output_path)

# Test function for dither_image with a color palette of 6 colors
def test_dither_image_six_colors(temp_png_file):
    """
    Tests the dither_image function with a color palette of 6 colors.
    """
    img = Image.new("RGB", (10, 10), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 3, 3), fill=(0, 0, 0))
    draw.rectangle((4, 4, 7, 7), fill=(128, 128, 128))
    draw.rectangle((8, 8, 9, 9), fill=(255, 0, 0))
    draw.rectangle((1, 1, 4, 4), fill=(0, 255, 0))
    draw.rectangle((5, 5, 8, 8), fill=(0, 0, 255))
    
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_six_colors.png")
    img.save(img_path)
    
    dither_image(img_path)
    
    # Check if the output file exists
    output_path = f"{img_path.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the temporary file and output file after test
    os.remove(img_path)
    os.remove(output_path)

# Test function for dither_image with a color palette of 7 colors
def test_dither_image_seven_colors(temp_png_file):
    """
    Tests the dither_image function with a color palette of 7 colors.
    """
    img = Image.new("RGB", (10, 10), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 3, 3), fill=(0, 0, 0))
    draw.rectangle((4, 4, 7, 7), fill=(128, 128, 128))
    draw.rectangle((8, 8, 9, 9), fill=(255, 0, 0))
    draw.rectangle((1, 1, 4, 4), fill=(0, 255, 0))
    draw.rectangle((5, 5, 8, 8), fill=(0, 0, 255))
    draw.rectangle((2, 2, 5, 5), fill=(255, 255, 0))
    
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_seven_colors.png")
    img.save(img_path)
    
    dither_image(img_path)
    
    # Check if the output file exists
    output_path = f"{img_path.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the temporary file and output file after test
    os.remove(img_path)
    os.remove(output_path)

# Test function for dither_image with a color palette of 8 colors
def test_dither_image_eight_colors(temp_png_file):
    """
    Tests the dither_image function with a color palette of 8 colors.
    """
    img = Image.new("RGB", (10, 10), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 3, 3), fill=(0, 0, 0))
    draw.rectangle((4, 4, 7, 7), fill=(128, 128, 128))
    draw.rectangle((8, 8, 9, 9), fill=(255, 0, 0))
    draw.rectangle((1, 1, 4, 4), fill=(0, 255, 0))
    draw.rectangle((5, 5, 8, 8), fill=(0, 0, 255))
    draw.rectangle((2, 2, 5, 5), fill=(255, 255, 0))
    draw.rectangle((3, 3, 6, 6), fill=(128, 0, 128))
    
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_eight_colors.png")
    img.save(img_path)
    
    dither_image(img_path)
    
    # Check if the output file exists
    output_path = f"{img_path.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the temporary file and output file after test
    os.remove(img_path)
    os.remove(output_path)

# Test function for dither_image with a color palette of 9 colors
def test_dither_image_nine_colors(temp_png_file):
    """
    Tests the dither_image function with a color palette of 9 colors.
    """
    img = Image.new("RGB", (10, 10), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 3, 3), fill=(0, 0, 0))
    draw.rectangle((4, 4, 7, 7), fill=(128, 128, 128))
    draw.rectangle((8, 8, 9, 9), fill=(255, 0, 0))
    draw.rectangle((1, 1, 4, 4), fill=(0, 255, 0))
    draw.rectangle((5, 5, 8, 8), fill=(0, 0, 255))
    draw.rectangle((2, 2, 5, 5), fill=(255, 255, 0))
    draw.rectangle((3, 3, 6, 6), fill=(128, 0, 128))
    draw.rectangle((4, 4, 7, 7), fill=(0, 128, 128))
    
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_nine_colors.png")
    img.save(img_path)
    
    dither_image(img_path)
    
    # Check if the output file exists
    output_path = f"{img_path.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the temporary file and output file after test
    os.remove(img_path)
    os.remove(output_path)

# Test function for dither_image with a color palette of 10 colors
def test_dither_image_ten_colors(temp_png_file):
    """
    Tests the dither_image function with a color palette of 10 colors.
    """
    img = Image.new("RGB", (10, 10), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 3, 3), fill=(0, 0, 0))
    draw.rectangle((4, 4, 7, 7), fill=(128, 128, 128))
    draw.rectangle((8, 8, 9, 9), fill=(255, 0, 0))
    draw.rectangle((1, 1, 4, 4), fill=(0, 255, 0))
    draw.rectangle((5, 5, 8, 8), fill=(0, 0, 255))
    draw.rectangle((2, 2, 5, 5), fill=(255, 255, 0))
    draw.rectangle((3, 3, 6, 6), fill=(128, 0, 128))
    draw.rectangle((4, 4, 7, 7), fill=(0, 128, 128))
    draw.rectangle((5, 5, 8, 8), fill=(128, 128, 0))
    
    img_path = os.path.join(os.path.dirname(temp_png_file), "test_ten_colors.png")
    img.save(img_path)
    
    dither_image(img_path)
    
    # Check if the output file exists
    output_path = f"{img_path.split('.')[0]}_dithered.png"
    assert os.path.exists(output_path), "Output file does not exist."
    
    # Clean up the temporary file and output file after test
    os.remove(img_path)
    os.remove(output_path)

# Test function for dither_image with a color palette of 11 colors
def test_dither_image_eleven_colors(temp_png_file):
    """
    Tests the dither_image function with a color palette of 11 colors.
    """
    img = Image.new("RGB", (10, 10), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 3, 3), fill=(0, 0, 0))
    draw.rectangle((4, 4, 7, 7), fill=(128, 128, 128))
    draw.rectangle((8, 8, 9, 9), fill=(255, 0, 0))
    draw.rectangle((1, 1, 4, 4), fill=(0, 255, 0))
    draw.rectangle((5, 5, 8, 8), fill=(0, 0, 255))
    draw.rectangle((2, 2, 5, 5), fill=(255, 255, 0))
    draw.rectangle((3