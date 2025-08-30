import random
from PIL import Image

def compress_image(input_path, output_path, percentage=0.1):
    """
    Compresses an image by introducing random pixel errors or artifacts.
    
    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path where the compressed image will be saved.
        percentage (float): Percentage of pixels to modify for glitch effects.
            Default is 0.1 (10%).
    """
    # Load the input image
    img = Image.open(input_path)
    width, height = img.size
    
    # Calculate how many pixels to change
    num_pixels = width * height
    change_count = int(num_pixels * percentage)
    
    # Create a new image with same size
    new_img = Image.new('RGB', (width, height))
    
    # Generate random colors for the changes
    for i in range(change_count):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        new_img.putpixel((x, y), (r, g, b))
    
    # Save the compressed image
    new_img.save(output_path, 'PNG')

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python BATCH2_PROMPT7_{{model_name}}.py input_image output_image")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    compress_image(input_path, output_path)

# ===== GENERATED TESTS =====
import os
from io import BytesIO
from PIL import Image
import pytest

# Original script code remains unchanged

def test_compress_image(tmp_path):
    """
    Test the compress_image function with a sample image.
    
    Args:
        tmp_path (Path): Temporary path for creating and saving test files.
    """
    # Create a temporary input image
    input_img = Image.new('RGB', (100, 100), color='red')
    input_path = os.path.join(tmp_path, 'input.png')
    input_img.save(input_path)
    
    # Define the output path
    output_path = os.path.join(tmp_path, 'output.png')
    
    # Call the compress_image function
    compress_image(input_path, output_path)
    
    # Load the compressed image and check its size
    compressed_img = Image.open(output_path)
    assert compressed_img.size == (100, 100), "The image dimensions are incorrect."
    
    # Check if the output file exists
    assert os.path.exists(output_path), "Output file does not exist."

def test_compress_image_with_percentage(tmp_path):
    """
    Test the compress_image function with different percentage values.
    
    Args:
        tmp_path (Path): Temporary path for creating and saving test files.
    """
    # Create a temporary input image
    input_img = Image.new('RGB', (100, 100), color='blue')
    input_path = os.path.join(tmp_path, 'input.png')
    input_img.save(input_path)
    
    # Define the output path
    output_path = os.path.join(tmp_path, 'output.png')
    
    # Test with different percentage values
    for percentage in [0.1, 0.5, 0.9]:
        compress_image(input_path, output_path, percentage=percentage)
        
        # Load the compressed image and check its size
        compressed_img = Image.open(output_path)
        assert compressed_img.size == (100, 100), f"The image dimensions are incorrect for percentage {percentage}."
        
        # Check if the output file exists
        assert os.path.exists(output_path), f"Output file does not exist for percentage {percentage}."

def test_compress_image_with_invalid_percentage(tmp_path):
    """
    Test the compress_image function with invalid percentage values.
    
    Args:
        tmp_path (Path): Temporary path for creating and saving test files.
    """
    # Create a temporary input image
    input_img = Image.new('RGB', (100, 100), color='green')
    input_path = os.path.join(tmp_path, 'input.png')
    input_img.save(input_path)
    
    # Define the output path
    output_path = os.path.join(tmp_path, 'output.png')
    
    # Test with invalid percentage values
    for percentage in [-1, 1.5]:
        with pytest.raises(ValueError):
            compress_image(input_path, output_path, percentage=percentage)

def test_compress_image_with_nonexistent_input_file(tmp_path):
    """
    Test the compress_image function with a non-existent input file.
    
    Args:
        tmp_path (Path): Temporary path for creating and saving test files.
    """
    # Define the non-existent input path
    input_path = os.path.join(tmp_path, 'non_existent.png')
    
    # Define the output path
    output_path = os.path.join(tmp_path, 'output.png')
    
    with pytest.raises(FileNotFoundError):
        compress_image(input_path, output_path)

def test_compress_image_with_invalid_output_path(tmp_path):
    """
    Test the compress_image function with an invalid output path.
    
    Args:
        tmp_path (Path): Temporary path for creating and saving test files.
    """
    # Create a temporary input image
    input_img = Image.new('RGB', (100, 100), color='yellow')
    input_path = os.path.join(tmp_path, 'input.png')
    input_img.save(input_path)
    
    # Define an invalid output path
    output_path = '/nonexistent/path/output.png'
    
    with pytest.raises(PermissionError):
        compress_image(input_path, output_path)

# Test cases follow the requirements above
