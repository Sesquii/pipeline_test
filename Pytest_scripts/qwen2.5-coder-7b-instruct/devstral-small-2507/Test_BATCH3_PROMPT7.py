# BATCH3_PROMPT7_Devstral.py

from PIL import Image
import random

def add_random_artifacts(image, artifact_probability=0.01):
    """
    Introduce random pixel artifacts in an image.

    Args:
        image (Image): The input PIL Image object.
        artifact_probability (float): Probability of altering a pixel (default: 0.01).

    Returns:
        Image: The modified image with random artifacts.
    """
    pixels = image.load()  # Load pixel data
    width, height = image.size

    for y in range(height):
        for x in range(width):
            if random.random() < artifact_probability:
                # Introduce random color changes to selected pixels
                r, g, b = pixels[x, y]
                new_r = min(255, max(0, r + random.randint(-30, 30)))
                new_g = min(255, max(0, g + random.randint(-30, 30)))  
                new_b = min(255, max(0, b + random.randint(-30, 30)))
                pixels[x, y] = (new_r, new_g, new_b)

    return image

def glitchy_compress(input_path, output_path, artifact_probability=0.01):
    """
    Compress an image by adding random artifacts.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the compressed image.
        artifact_probability (float): Probability of altering a pixel (default: 0.01).
    """
    try:
        with Image.open(input_path) as img:
            modified_img = add_random_artifacts(img, artifact_probability)
            modified_img.save(output_path, optimize=True, quality=85)
            print(f"Image saved to {output_path} with glitchy compression applied.")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    # Example usage
    input_image = "input.jpg"
    output_image = "glitchy_compressed.jpg"

    try:
        glitchy_compress(input_image, output_image, artifact_probability=0.02)
    except Exception as e:
        print(f"Error: {e}")

# ===== GENERATED TESTS =====
```python
# BATCH3_PROMPT7_Devstral.py

from PIL import Image
import random
import pytest
from io import BytesIO

def add_random_artifacts(image, artifact_probability=0.01):
    """
    Introduce random pixel artifacts in an image.

    Args:
        image (Image): The input PIL Image object.
        artifact_probability (float): Probability of altering a pixel (default: 0.01).

    Returns:
        Image: The modified image with random artifacts.
    """
    pixels = image.load()  # Load pixel data
    width, height = image.size

    for y in range(height):
        for x in range(width):
            if random.random() < artifact_probability:
                # Introduce random color changes to selected pixels
                r, g, b = pixels[x, y]
                new_r = min(255, max(0, r + random.randint(-30, 30)))
                new_g = min(255, max(0, g + random.randint(-30, 30)))  
                new_b = min(255, max(0, b + random.randint(-30, 30)))
                pixels[x, y] = (new_r, new_g, new_b)

    return image

def glitchy_compress(input_path, output_path, artifact_probability=0.01):
    """
    Compress an image by adding random artifacts.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the compressed image.
        artifact_probability (float): Probability of altering a pixel (default: 0.01).
    """
    try:
        with Image.open(input_path) as img:
            modified_img = add_random_artifacts(img, artifact_probability)
            modified_img.save(output_path, optimize=True, quality=85)
            print(f"Image saved to {output_path} with glitchy compression applied.")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    # Example usage
    input_image = "input.jpg"
    output_image = "glitchy_compressed.jpg"

    try:
        glitchy_compress(input_image, output_image, artifact_probability=0.02)
    except Exception as e:
        print(f"Error: {e}")

# Test suite for BATCH3_PROMPT7_Devstral.py

def test_add_random_artifacts():
    """Test the add_random_artifacts function."""
    # Create a small image
    img = Image.new('RGB', (10, 10), color='white')
    modified_img = add_random_artifacts(img)

    # Check if any pixel has changed
    pixels = modified_img.load()
    changed_pixels = sum(1 for y in range(10) for x in range(10) if pixels[x, y] != (255, 255, 255))
    
    assert changed_pixels > 0

def test_glitchy_compress(tmp_path):
    """Test the glitchy_compress function."""
    # Create a small image
    img = Image.new('RGB', (10, 10), color='white')
    input_path = tmp_path / 'input.jpg'
    output_path = tmp_path / 'glitchy_compressed.jpg'

    # Save the image to the temporary path
    img.save(input_path)

    # Call the glitchy_compress function
    glitchy_compress(str(input_path), str(output_path))

    # Check if the output file exists and is not empty
    assert output_path.exists()
    assert output_path.stat().st_size > 0

def test_glitchy_compress_with_artifact_probability(tmp_path):
    """Test the glitchy_compress function with different artifact probabilities."""
    # Create a small image
    img = Image.new('RGB', (10, 10), color='white')
    input_path = tmp_path / 'input.jpg'
    output_path = tmp_path / 'glitchy_compressed.jpg'

    # Save the image to the temporary path
    img.save(input_path)

    # Call the glitchy_compress function with different artifact probabilities
    for prob in [0.01, 0.1, 0.5]:
        glitchy_compress(str(input_path), str(output_path), artifact_probability=prob)
        
        # Check if the output file exists and is not empty
        assert output_path.exists()
        assert output_path.stat().st_size > 0

def test_glitchy_compress_with_invalid_input(tmp_path):
    """Test the glitchy_compress function with invalid input."""
    # Create a non-existent image path
    input_path = tmp_path / 'non_existent.jpg'
    output_path = tmp_path / 'glitchy_compressed.jpg'

    # Call the glitchy_compress function with invalid input
    with pytest.raises(Exception):
        glitchy_compress(str(input_path), str(output_path))

def test_glitchy_compress_with_invalid_output(tmp_path):
    """Test the glitchy_compress function with invalid output."""
    # Create a small image
    img = Image.new('RGB', (10, 10), color='white')
    input_path = tmp_path / 'input.jpg'
    output_path = tmp_path / 'invalid_output'

    # Save the image to the temporary path
    img.save(input_path)

    # Call the glitchy_compress function with invalid output
    with pytest.raises(Exception):
        glitchy_compress(str(input_path), str(output_path))
```