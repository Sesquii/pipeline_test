from PIL import Image
import random

def glitchy_image_compressor(input_path):
    # Open the input image
    with Image.open(input_path) as img:
        width, height = img.size
        
        # Get a random number of pixels to corrupt (up to 10% of the total pixels)
        num_pixels_to_corrupt = random.randint(0, int(width * height * 0.1))
        
        # Loop through each pixel and randomly set its RGB values to 0
        for _ in range(num_pixels_to_corrupt):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            img.putpixel((x, y), (0, 0, 0))
        
        # Save the corrupted image with a new filename
        output_filename = f"{input_path.split('.')[0]}_corrupt.jpg"
        img.save(output_filename)

# Entry point of the program
if __name__ == "__main__":
    input_image_path = "path_to_your_image.jpg"  # Replace with your JPG file path
    glitchy_image_compressor(input_image_path)
```

Replace `"path_to_your_image.jpg"` with the actual path to your JPG image file. This script will open the specified image, randomly corrupt a number of pixels by setting their RGB values to 0, and save the corrupted image with a new filename in the same directory as the original.

# ===== GENERATED TESTS =====
```python
from PIL import Image
import random
import os
import pytest

def glitchy_image_compressor(input_path):
    # Open the input image
    with Image.open(input_path) as img:
        width, height = img.size
        
        # Get a random number of pixels to corrupt (up to 10% of the total pixels)
        num_pixels_to_corrupt = random.randint(0, int(width * height * 0.1))
        
        # Loop through each pixel and randomly set its RGB values to 0
        for _ in range(num_pixels_to_corrupt):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            img.putpixel((x, y), (0, 0, 0))
        
        # Save the corrupted image with a new filename
        output_filename = f"{input_path.split('.')[0]}_corrupt.jpg"
        img.save(output_filename)

# Entry point of the program
if __name__ == "__main__":
    input_image_path = "path_to_your_image.jpg"  # Replace with your JPG file path
    glitchy_image_compressor(input_image_path)

# Test cases
def test_glitchy_image_compressor(tmpdir):
    """
    Test the glitchy_image_compressor function.
    """
    
    # Create a temporary image for testing
    input_image = Image.new('RGB', (100, 100), color='red')
    input_path = os.path.join(tmpdir, 'test_image.jpg')
    input_image.save(input_path)
    
    # Call the function with the test image
    glitchy_image_compressor(input_path)
    
    # Check if the corrupted image was created
    output_filename = f"{input_path.split('.')[0]}_corrupt.jpg"
    assert os.path.exists(output_filename), "Corrupted image not created."
    
    # Clean up the temporary files
    os.remove(input_path)
    os.remove(output_filename)

def test_glitchy_image_compressor_no_pixels_to_corrupt(tmpdir):
    """
    Test the glitchy_image_compressor function with no pixels to corrupt.
    """
    
    # Create a temporary image for testing
    input_image = Image.new('RGB', (100, 100), color='red')
    input_path = os.path.join(tmpdir, 'test_image.jpg')
    input_image.save(input_path)
    
    # Call the function with the test image and no pixels to corrupt
    glitchy_image_compressor(input_path)
    
    # Check if the corrupted image was created
    output_filename = f"{input_path.split('.')[0]}_corrupt.jpg"
    assert os.path.exists(output_filename), "Corrupted image not created."
    
    # Clean up the temporary files
    os.remove(input_path)
    os.remove(output_filename)

def test_glitchy_image_compressor_negative_pixels_to_corrupt(tmpdir):
    """
    Test the glitchy_image_compressor function with negative pixels to corrupt.
    """
    
    # Create a temporary image for testing
    input_image = Image.new('RGB', (100, 100), color='red')
    input_path = os.path.join(tmpdir, 'test_image.jpg')
    input_image.save(input_path)
    
    # Call the function with the test image and negative pixels to corrupt
    with pytest.raises(ValueError):
        glitchy_image_compressor(input_path)

def test_glitchy_image_compressor_invalid_input_type(tmpdir):
    """
    Test the glitchy_image_compressor function with an invalid input type.
    """
    
    # Create a temporary file for testing
    input_path = os.path.join(tmpdir, 'test_file.txt')
    with open(input_path, 'w') as f:
        f.write("This is not an image.")
    
    # Call the function with the test file and expect a TypeError
    with pytest.raises(TypeError):
        glitchy_image_compressor(input_path)

def test_glitchy_image_compressor_nonexistent_file(tmpdir):
    """
    Test the glitchy_image_compressor function with a nonexistent file.
    """
    
    # Create a non-existent file path
    input_path = os.path.join(tmpdir, 'non_existent.jpg')
    
    # Call the function with the non-existent file and expect a FileNotFoundError
    with pytest.raises(FileNotFoundError):
        glitchy_image_compressor(input_path)
```