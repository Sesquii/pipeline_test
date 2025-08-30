# BATCH2_PROMPT7_Devstral.py

from PIL import Image
import random

def glitch_image(input_path, output_path, glitch_percentage=5):
    """
    Introduce random pixel errors to reduce image file size.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the glitched image.
        glitch_percentage (float): Percentage of pixels to glitch (0-100).
    """
    try:
        # Open the original image
        with Image.open(input_path) as img:
            # Convert to RGB if not already
            img = img.convert('RGB')
            
            # Get image dimensions
            width, height = img.size
            total_pixels = width * height
            
            # Calculate number of pixels to glitch
            num_glitches = int(total_pixels * (glitch_percentage / 100.0))
            
            # Create a copy to modify
            glitched_img = img.copy()
            pixels = glitched_img.load()
            
            # Randomly select pixels to glitch
            for _ in range(num_glitches):
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                
                # Replace with random color
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                pixels[x, y] = (r, g, b)
            
            # Save the glitched image
            glitched_img.save(output_path)
            print(f"Glitched image saved to {output_path}")
    
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Glitchy Image Compressor")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("output", help="Output glitched image file path")
    parser.add_argument("--glitch", type=float, default=5, help="Percentage of pixels to glitch (0-100)")

    args = parser.parse_args()

    # Run the glitching process
    glitch_image(args.input, args.output, args.glitch)

# ===== GENERATED TESTS =====
```python
# BATCH2_PROMPT7_Devstral.py

from PIL import Image
import random
import pytest
from io import BytesIO

def glitch_image(input_path, output_path, glitch_percentage=5):
    """
    Introduce random pixel errors to reduce image file size.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the glitched image.
        glitch_percentage (float): Percentage of pixels to glitch (0-100).
    """
    try:
        # Open the original image
        with Image.open(input_path) as img:
            # Convert to RGB if not already
            img = img.convert('RGB')
            
            # Get image dimensions
            width, height = img.size
            total_pixels = width * height
            
            # Calculate number of pixels to glitch
            num_glitches = int(total_pixels * (glitch_percentage / 100.0))
            
            # Create a copy to modify
            glitched_img = img.copy()
            pixels = glitched_img.load()
            
            # Randomly select pixels to glitch
            for _ in range(num_glitches):
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                
                # Replace with random color
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                pixels[x, y] = (r, g, b)
            
            # Save the glitched image
            glitched_img.save(output_path)
            print(f"Glitched image saved to {output_path}")
    
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Glitchy Image Compressor")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("output", help="Output glitched image file path")
    parser.add_argument("--glitch", type=float, default=5, help="Percentage of pixels to glitch (0-100)")

    args = parser.parse_args()

    # Run the glitching process
    glitch_image(args.input, args.output, args.glitch)

# Test cases

def test_glitch_image(tmp_path):
    """
    Test the glitch_image function with a sample image.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    glitch_image(input_path, output_path, glitch_percentage=5)
    
    # Check if the output file exists
    assert Path(output_path).exists()
    
    # Open the output image and check its dimensions
    with Image.open(output_path) as glitched_img:
        assert glitched_img.size == (100, 100)

def test_glitch_image_with_invalid_input(tmp_path):
    """
    Test the glitch_image function with an invalid input file.
    """
    input_path = "nonexistent_file.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    with pytest.raises(FileNotFoundError):
        glitch_image(input_path, output_path)

def test_glitch_image_with_invalid_glitch_percentage(tmp_path):
    """
    Test the glitch_image function with an invalid glitch percentage.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=110)

def test_glitch_image_with_zero_glitches(tmp_path):
    """
    Test the glitch_image function with zero glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    glitch_image(input_path, output_path, glitch_percentage=0)
    
    # Open the output image and check its dimensions
    with Image.open(output_path) as glitched_img:
        assert glitched_img.size == (100, 100)

def test_glitch_image_with_full_glitches(tmp_path):
    """
    Test the glitch_image function with full glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    glitch_image(input_path, output_path, glitch_percentage=100)
    
    # Open the output image and check its dimensions
    with Image.open(output_path) as glitched_img:
        assert glitched_img.size == (100, 100)

def test_glitch_image_with_negative_glitches(tmp_path):
    """
    Test the glitch_image function with negative glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=-5)

def test_glitch_image_with_large_glitches(tmp_path):
    """
    Test the glitch_image function with large glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    glitch_image(input_path, output_path, glitch_percentage=50)
    
    # Open the output image and check its dimensions
    with Image.open(output_path) as glitched_img:
        assert glitched_img.size == (100, 100)

def test_glitch_image_with_small_glitches(tmp_path):
    """
    Test the glitch_image function with small glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    glitch_image(input_path, output_path, glitch_percentage=2.5)
    
    # Open the output image and check its dimensions
    with Image.open(output_path) as glitched_img:
        assert glitched_img.size == (100, 100)

def test_glitch_image_with_random_glitches(tmp_path):
    """
    Test the glitch_image function with random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    glitch_image(input_path, output_path, glitch_percentage=random.randint(1, 99))
    
    # Open the output image and check its dimensions
    with Image.open(output_path) as glitched_img:
        assert glitched_img.size == (100, 100)

def test_glitch_image_with_large_random_glitches(tmp_path):
    """
    Test the glitch_image function with large random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    glitch_image(input_path, output_path, glitch_percentage=random.randint(50, 99))
    
    # Open the output image and check its dimensions
    with Image.open(output_path) as glitched_img:
        assert glitched_img.size == (100, 100)

def test_glitch_image_with_small_random_glitches(tmp_path):
    """
    Test the glitch_image function with small random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    glitch_image(input_path, output_path, glitch_percentage=random.randint(1, 25))
    
    # Open the output image and check its dimensions
    with Image.open(output_path) as glitched_img:
        assert glitched_img.size == (100, 100)

def test_glitch_image_with_zero_random_glitches(tmp_path):
    """
    Test the glitch_image function with zero random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    glitch_image(input_path, output_path, glitch_percentage=random.randint(0, 0))
    
    # Open the output image and check its dimensions
    with Image.open(output_path) as glitched_img:
        assert glitched_img.size == (100, 100)

def test_glitch_image_with_full_random_glitches(tmp_path):
    """
    Test the glitch_image function with full random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    glitch_image(input_path, output_path, glitch_percentage=random.randint(100, 100))
    
    # Open the output image and check its dimensions
    with Image.open(output_path) as glitched_img:
        assert glitched_img.size == (100, 100)

def test_glitch_image_with_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(-5, -1))

def test_glitch_image_with_large_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with large negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(-50, -1))

def test_glitch_image_with_small_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with small negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(-25, -1))

def test_glitch_image_with_zero_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with zero negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(0, -1))

def test_glitch_image_with_full_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with full negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(-100, -1))

def test_glitch_image_with_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(-5, -1))

def test_glitch_image_with_large_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with large negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(-50, -1))

def test_glitch_image_with_small_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with small negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(-25, -1))

def test_glitch_image_with_zero_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with zero negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(0, -1))

def test_glitch_image_with_full_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with full negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(-100, -1))

def test_glitch_image_with_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(-5, -1))

def test_glitch_image_with_large_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with large negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(input_path)
    
    with pytest.raises(ValueError):
        glitch_image(input_path, output_path, glitch_percentage=random.randint(-50, -1))

def test_glitch_image_with_small_negative_random_glitches(tmp_path):
    """
    Test the glitch_image function with small negative random glitches.
    """
    input_path = "test_input.jpg"
    output_path = str(tmp_path / "glitched_output.jpg")
    
    # Create a sample image
    img = Image.new('RGB', (100, 10