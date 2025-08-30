#!/usr/bin/env python3

import os
from PIL import Image
import random

def glitch_image(input_path, output_path):
    # Open the image using Pillow
    with Image.open(input_path) as img:
        width, height = img.size
        
        # Convert image to RGB mode if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Create a new image to hold the glitched version
        glitch_img = img.copy()
        
        # Introduce pixel errors randomly
        for x in range(width):
            for y in range(height):
                if random.random() < 0.1:  # 10% chance to glitch a pixel
                    glitch_img.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        
        # Save the glitched image
        glitch_img.save(output_path)

if __name__ == "__main__":
    input_image = 'input.jpg'  # Replace with your input image path
    output_image = 'output_glitched.jpg'  # Replace with desired output path
    
    if not os.path.exists(input_image):
        print(f"Error: Input file {input_image} does not exist.")
    else:
        glitch_image(input_image, output_image)
        print(f"Glitchy image saved as {output_image}")

This Python script uses the Pillow library to open an image and introduces random pixel errors (artifacts) to simulate a "glitched" effect. The probability of introducing an error is 10%. The glitched image is then saved to the specified output path.

# ===== GENERATED TESTS =====
#!/usr/bin/env python3

import os
from PIL import Image
import random
import pytest

def glitch_image(input_path, output_path):
    # Open the image using Pillow
    with Image.open(input_path) as img:
        width, height = img.size
        
        # Convert image to RGB mode if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Create a new image to hold the glitched version
        glitch_img = img.copy()
        
        # Introduce pixel errors randomly
        for x in range(width):
            for y in range(height):
                if random.random() < 0.1:  # 10% chance to glitch a pixel
                    glitch_img.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        
        # Save the glitched image
        glitch_img.save(output_path)

if __name__ == "__main__":
    input_image = 'input.jpg'  # Replace with your input image path
    output_image = 'output_glitched.jpg'  # Replace with desired output path
    
    if not os.path.exists(input_image):
        print(f"Error: Input file {input_image} does not exist.")
    else:
        glitch_image(input_image, output_image)
        print(f"Glitchy image saved as {output_image}")

# Test suite for the glitch_image function
def test_glitch_image(tmpdir):
    """
    Test the glitch_image function with a sample input and verify that the output file is created.
    """
    input_path = os.path.join(tmpdir, 'input.jpg')
    output_path = os.path.join(tmpdir, 'output_glitched.jpg')
    
    # Create a sample image for testing
    img = Image.new('RGB', (100, 100), color='red')
    img.save(input_path)
    
    glitch_image(input_path, output_path)
    
    assert os.path.exists(output_path), "Output file does not exist"
    
def test_glitch_image_with_nonexistent_input(tmpdir):
    """
    Test the glitch_image function with a non-existent input file and verify that an error message is printed.
    """
    input_path = os.path.join(tmpdir, 'nonexistent.jpg')
    output_path = os.path.join(tmpdir, 'output_glitched.jpg')
    
    # Attempt to glitch the image
    with pytest.raises(SystemExit) as excinfo:
        glitch_image(input_path, output_path)
    
    assert "Error: Input file" in str(excinfo.value), "Expected error message not found"

def test_glitch_image_with_non_rgb_input(tmpdir):
    """
    Test the glitch_image function with a non-RGB input image and verify that it is converted to RGB.
    """
    input_path = os.path.join(tmpdir, 'input.png')
    output_path = os.path.join(tmpdir, 'output_glitched.jpg')
    
    # Create a sample PNG image for testing
    img = Image.new('RGBA', (100, 100), color='red')
    img.save(input_path)
    
    glitch_image(input_path, output_path)
    
    with Image.open(output_path) as glitched_img:
        assert glitched_img.mode == 'RGB', "Output image is not in RGB mode"

def test_glitch_image_with_custom_probability(tmpdir):
    """
    Test the glitch_image function with a custom probability of 5% and verify that fewer pixels are glitched.
    """
    input_path = os.path.join(tmpdir, 'input.jpg')
    output_path = os.path.join(tmpdir, 'output_glitched.jpg')
    
    # Create a sample image for testing
    img = Image.new('RGB', (100, 100), color='red')
    img.save(input_path)
    
    # Save the original image as a reference
    img.save(os.path.join(tmpdir, 'original.jpg'))
    
    glitch_image(input_path, output_path, probability=0.05)
    
    with Image.open(output_path) as glitched_img:
        with Image.open(os.path.join(tmpdir, 'original.jpg')) as original_img:
            assert sum(1 for x in range(original_img.width) for y in range(original_img.height) if glitched_img.getpixel((x, y)) != original_img.getpixel((x, y))) < 500, "Too many pixels are glitched"

# Test cases using pytest fixtures and parametrization
@pytest.fixture(params=[(100, 100), (200, 300)])
def image_size(request):
    """
    Fixture to provide different image sizes for testing.
    """
    return request.param

def test_glitch_image_with_different_sizes(image_size, tmpdir):
    """
    Test the glitch_image function with different image sizes and verify that the output file is created.
    """
    input_path = os.path.join(tmpdir, 'input.jpg')
    output_path = os.path.join(tmpdir, 'output_glitched.jpg')
    
    # Create a sample image for testing
    img = Image.new('RGB', image_size, color='red')
    img.save(input_path)
    
    glitch_image(input_path, output_path)
    
    assert os.path.exists(output_path), "Output file does not exist"

def test_glitch_image_with_probability_zero(image_size, tmpdir):
    """
    Test the glitch_image function with a probability of 0 and verify that no pixels are glitched.
    """
    input_path = os.path.join(tmpdir, 'input.jpg')
    output_path = os.path.join(tmpdir, 'output_glitched.jpg')
    
    # Create a sample image for testing
    img = Image.new('RGB', image_size, color='red')
    img.save(input_path)
    
    glitch_image(input_path, output_path, probability=0.0)
    
    with Image.open(output_path) as glitched_img:
        assert all(glitched_img.getpixel((x, y)) == (255, 0, 0) for x in range(image_size[0]) for y in range(image_size[1])), "Some pixels are glitched"

# Test cases using pytest fixtures and parametrization with custom probability
@pytest.fixture(params=[0.05, 0.15])
def custom_probability(request):
    """
    Fixture to provide different custom probabilities for testing.
    """
    return request.param

def test_glitch_image_with_custom_probabilities(custom_probability, image_size, tmpdir):
    """
    Test the glitch_image function with different custom probabilities and verify that the output file is created.
    """
    input_path = os.path.join(tmpdir, 'input.jpg')
    output_path = os.path.join(tmpdir, 'output_glitched.jpg')
    
    # Create a sample image for testing
    img = Image.new('RGB', image_size, color='red')
    img.save(input_path)
    
    glitch_image(input_path, output_path, probability=custom_probability)
    
    assert os.path.exists(output_path), "Output file does not exist"

def test_glitch_image_with_custom_probabilities_and_different_sizes(custom_probability, image_size, tmpdir):
    """
    Test the glitch_image function with different custom probabilities and different image sizes and verify that the output file is created.
    """
    input_path = os.path.join(tmpdir, 'input.jpg')
    output_path = os.path.join(tmpdir, 'output_glitched.jpg')
    
    # Create a sample image for testing
    img = Image.new('RGB', image_size, color='red')
    img.save(input_path)
    
    glitch_image(input_path, output_path, probability=custom_probability)
    
    assert os.path.exists(output_path), "Output file does not exist"

This test suite includes comprehensive test cases for the `glitch_image` function. It covers various scenarios such as different image sizes, custom probabilities, and non-existent input files. The test cases use pytest fixtures and parametrization to ensure that the function behaves correctly under different conditions.