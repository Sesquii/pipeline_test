import cv2
import numpy as np
import sys

def apply_color_glitch(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found.")
        return
    
    # Get dimensions of the image
    height, width, _ = img.shape
    
    # Define a random portion to glitch (50x50 pixels in this example)
    x = np.random.randint(0, width - 50)
    y = np.random.randint(0, height - 50)
    
    # Swap color channels
    temp = img[y:y+50, x:x+50, 0].copy()
    img[y:y+50, x:x+50, 0] = img[y:y+50, x:x+50, 2]
    img[y:y+50, x:x+50, 2] = temp
    
    # Save the glitched image
    output_path = f"{image_path}_color_glitch.png"
    cv2.imwrite(output_path, img)
    
    print(f"Glitched image saved as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python glitchy_image_compressor.py <image_file_path>")
    else:
        apply_color_glitch(sys.argv[1])

This Python script uses the `OpenCV` library to read an image, introduce a color glitch by swapping a portion of the color channels, and save the glitched image. The script takes an image file path as a command-line argument.

# ===== GENERATED TESTS =====
import pytest
from io import BytesIO
import cv2
import numpy as np

# Original code remains unchanged

def apply_color_glitch(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found.")
        return
    
    # Get dimensions of the image
    height, width, _ = img.shape
    
    # Define a random portion to glitch (50x50 pixels in this example)
    x = np.random.randint(0, width - 50)
    y = np.random.randint(0, height - 50)
    
    # Swap color channels
    temp = img[y:y+50, x:x+50, 0].copy()
    img[y:y+50, x:x+50, 0] = img[y:y+50, x:x+50, 2]
    img[y:y+50, x:x+50, 2] = temp
    
    # Save the glitched image
    output_path = f"{image_path}_color_glitch.png"
    cv2.imwrite(output_path, img)
    
    print(f"Glitched image saved as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python glitchy_image_compressor.py <image_file_path>")
    else:
        apply_color_glitch(sys.argv[1])

# Test suite starts here

def test_apply_color_glitch_with_valid_image(mocker):
    """Test the apply_color_glitch function with a valid image."""
    # Mock cv2.imread to return a dummy image
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "dummy_image_color_glitch.png"
    apply_color_glitch("dummy_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_nonexistent_image(mocker):
    """Test the apply_color_glitch function with a non-existent image."""
    mocker.patch('cv2.imread', return_value=None)
    
    output_path = "nonexistent_image_color_glitch.png"
    apply_color_glitch("nonexistent_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_invalid_image(mocker):
    """Test the apply_color_glitch function with an invalid image."""
    dummy_img = np.zeros((100, 100), dtype=np.uint8)  # Invalid image format (grayscale)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "invalid_image_color_glitch.png"
    apply_color_glitch("invalid_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_small_image(mocker):
    """Test the apply_color_glitch function with a small image."""
    dummy_img = np.zeros((50, 50, 3), dtype=np.uint8)  # Too small for glitching
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "small_image_color_glitch.png"
    apply_color_glitch("small_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_large_image(mocker):
    """Test the apply_color_glitch function with a large image."""
    dummy_img = np.zeros((1000, 1000, 3), dtype=np.uint8)  # Large image
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "large_image_color_glitch.png"
    apply_color_glitch("large_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_negative_x(mocker):
    """Test the apply_color_glitch function with a negative x value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "negative_x_image_color_glitch.png"
    apply_color_glitch("negative_x_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_negative_y(mocker):
    """Test the apply_color_glitch function with a negative y value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "negative_y_image_color_glitch.png"
    apply_color_glitch("negative_y_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_large_x(mocker):
    """Test the apply_color_glitch function with a large x value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "large_x_image_color_glitch.png"
    apply_color_glitch("large_x_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_large_y(mocker):
    """Test the apply_color_glitch function with a large y value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "large_y_image_color_glitch.png"
    apply_color_glitch("large_y_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_zero_x(mocker):
    """Test the apply_color_glitch function with a zero x value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "zero_x_image_color_glitch.png"
    apply_color_glitch("zero_x_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_zero_y(mocker):
    """Test the apply_color_glitch function with a zero y value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "zero_y_image_color_glitch.png"
    apply_color_glitch("zero_y_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_random_x(mocker):
    """Test the apply_color_glitch function with a random x value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "random_x_image_color_glitch.png"
    apply_color_glitch("random_x_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_random_y(mocker):
    """Test the apply_color_glitch function with a random y value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "random_y_image_color_glitch.png"
    apply_color_glitch("random_y_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_negative_width(mocker):
    """Test the apply_color_glitch function with a negative width value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "negative_width_image_color_glitch.png"
    apply_color_glitch("negative_width_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_negative_height(mocker):
    """Test the apply_color_glitch function with a negative height value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "negative_height_image_color_glitch.png"
    apply_color_glitch("negative_height_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_zero_width(mocker):
    """Test the apply_color_glitch function with a zero width value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "zero_width_image_color_glitch.png"
    apply_color_glitch("zero_width_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_zero_height(mocker):
    """Test the apply_color_glitch function with a zero height value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "zero_height_image_color_glitch.png"
    apply_color_glitch("zero_height_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_large_width(mocker):
    """Test the apply_color_glitch function with a large width value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "large_width_image_color_glitch.png"
    apply_color_glitch("large_width_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_large_height(mocker):
    """Test the apply_color_glitch function with a large height value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "large_height_image_color_glitch.png"
    apply_color_glitch("large_height_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_random_width(mocker):
    """Test the apply_color_glitch function with a random width value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "random_width_image_color_glitch.png"
    apply_color_glitch("random_width_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_random_height(mocker):
    """Test the apply_color_glitch function with a random height value."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "random_height_image_color_glitch.png"
    apply_color_glitch("random_height_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_negative_x_and_y(mocker):
    """Test the apply_color_glitch function with negative x and y values."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "negative_x_y_image_color_glitch.png"
    apply_color_glitch("negative_x_y_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_zero_x_and_y(mocker):
    """Test the apply_color_glitch function with zero x and y values."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "zero_x_y_image_color_glitch.png"
    apply_color_glitch("zero_x_y_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_large_x_and_y(mocker):
    """Test the apply_color_glitch function with large x and y values."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "large_x_y_image_color_glitch.png"
    apply_color_glitch("large_x_y_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_random_x_and_y(mocker):
    """Test the apply_color_glitch function with random x and y values."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "random_x_y_image_color_glitch.png"
    apply_color_glitch("random_x_y_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_negative_width_and_height(mocker):
    """Test the apply_color_glitch function with negative width and height values."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "negative_width_height_image_color_glitch.png"
    apply_color_glitch("negative_width_height_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_zero_width_and_height(mocker):
    """Test the apply_color_glitch function with zero width and height values."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "zero_width_height_image_color_glitch.png"
    apply_color_glitch("zero_width_height_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_large_width_and_height(mocker):
    """Test the apply_color_glitch function with large width and height values."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "large_width_height_image_color_glitch.png"
    apply_color_glitch("large_width_height_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_random_width_and_height(mocker):
    """Test the apply_color_glitch function with random width and height values."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "random_width_height_image_color_glitch.png"
    apply_color_glitch("random_width_height_image.jpg")
    
    # Check if cv2.imwrite was called with the correct arguments
    cv2.imwrite.assert_called_once_with(output_path, dummy_img)

def test_apply_color_glitch_with_negative_x_and_large_y(mocker):
    """Test the apply_color_glitch function with negative x and large y values."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "negative_x_large_y_image_color_glitch.png"
    apply_color_glitch("negative_x_large_y_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_negative_x_and_zero_y(mocker):
    """Test the apply_color_glitch function with negative x and zero y values."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "negative_x_zero_y_image_color_glitch.png"
    apply_color_glitch("negative_x_zero_y_image.jpg")
    
    # Check if cv2.imwrite was not called
    assert not cv2.imwrite.called

def test_apply_color_glitch_with_negative_x_and_small_y(mocker):
    """Test the apply_color_glitch function with negative x and small y values."""
    dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
    mocker.patch('cv2.imread', return_value=dummy_img)
    
    output_path = "negative_x_small_y_image_color_glitch.png"
    apply_color_glitch("negative_x_small_y_image.jpg")
    
    # Check if cv2.imwrite was not