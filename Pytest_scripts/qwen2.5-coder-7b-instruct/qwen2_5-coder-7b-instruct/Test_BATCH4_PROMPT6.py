import cv2
import numpy as np
import sys

def glitch_image(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Unable to load image.")
        return
    
    # Get image dimensions
    height, width, channels = img.shape
    
    # Define the portion of the image to glitch (e.g., 10% of the image in each dimension)
    glitch_height = int(height * 0.1)
    glitch_width = int(width * 0.1)
    
    # Calculate starting points for the glitch
    start_y = np.random.randint(0, height - glitch_height)
    start_x = np.random.randint(0, width - glitch_width)
    
    # Define the portion to swap
    glitch_portion = img[start_y:start_y+glitch_height, start_x:start_x+glitch_width]
    
    # Randomly shuffle the channels
    for i in range(channels):
        np.random.shuffle(glitch_portion[:, :, i])
    
    # Replace the original portion with the glitched one
    img[start_y:start_y+glitch_height, start_x:start_x+glitch_width] = glitch_portion
    
    # Save the glitched image
    output_path = f"{image_path.split('.')[0]}_color_glitch.png"
    cv2.imwrite(output_path, img)
    
    print(f"Glitched image saved as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python glitch_image.py <image_file_path>")
    else:
        glitch_image(sys.argv[1])
```

This Python script uses the `OpenCV` library to load and modify an image. It introduces a glitch by randomly swapping a portion of the color channels. The output is saved as `<input_filename>_color_glitch.png`.

# ===== GENERATED TESTS =====
```python
import pytest
from pathlib import Path
import numpy as np

# Original script code remains unchanged

def test_glitch_image(tmp_path):
    """Test the glitch_image function with a valid image file."""
    input_image = tmp_path / "test.jpg"
    input_image.write_bytes(cv2.imencode('.jpg', np.zeros((100, 100, 3), dtype=np.uint8))[1].tobytes())
    
    output_image = input_image.with_name(f"{input_image.stem}_color_glitch.png")
    
    glitch_image(str(input_image))
    
    assert output_image.exists()
    assert output_image.stat().st_size > 0

def test_glitch_image_invalid_path():
    """Test the glitch_image function with an invalid image file path."""
    with pytest.raises(SystemExit) as exc_info:
        glitch_image("nonexistent_file.jpg")
    
    assert exc_info.value.code == 1

def test_glitch_image_no_arguments(capsys):
    """Test the glitch_image function when no arguments are provided."""
    with pytest.raises(SystemExit) as exc_info:
        glitch_image()
    
    captured = capsys.readouterr()
    assert "Usage: python glitch_image.py <image_file_path>" in captured.out
    assert exc_info.value.code == 1

def test_glitch_image_with_arguments(capsys):
    """Test the glitch_image function with valid arguments."""
    input_image = Path("test.jpg")
    input_image.write_bytes(cv2.imencode('.jpg', np.zeros((100, 100, 3), dtype=np.uint8))[1].tobytes())
    
    output_image = input_image.with_name(f"{input_image.stem}_color_glitch.png")
    
    glitch_image(str(input_image))
    
    captured = capsys.readouterr()
    assert f"Glitched image saved as {output_image}" in captured.out
    assert output_image.exists()
    assert output_image.stat().st_size > 0

# Test cases using pytest fixtures and parametrization
@pytest.fixture(params=["test.jpg", "test.png"])
def test_images(request, tmp_path):
    input_image = tmp_path / request.param
    input_image.write_bytes(cv2.imencode(f'.{request.param.split(".")[1]}', np.zeros((100, 100, 3), dtype=np.uint8))[1].tobytes())
    yield input_image

def test_glitch_image_with_different_formats(test_images):
    output_image = test_images.with_name(f"{test_images.stem}_color_glitch.png")
    
    glitch_image(str(test_images))
    
    assert output_image.exists()
    assert output_image.stat().st_size > 0
```