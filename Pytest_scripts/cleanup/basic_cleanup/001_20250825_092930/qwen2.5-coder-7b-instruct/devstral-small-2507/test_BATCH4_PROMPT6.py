import cv2
import numpy as np
import sys
import os

def add_glitch(image):
    """Introduce a glitch by randomly swapping color channels."""
    height, width = image.shape[:2]

    # Randomly select a portion of the image to apply glitch
    x = np.random.randint(0, width - 1)
    y = np.random.randint(0, height - 1)
    w = np.random.randint(50, min(200, width - x))
    h = np.random.randint(50, min(200, height - y))

    # Extract the region to apply glitch
    region = image[y:y+h, x:x+w]

    # Randomly swap channels in the selected region
    if np.random.rand() > 0.5:
        region[:, :, [0, 1]] = region[:, :, [1, 0]]
    else:
        region[:, :, [1, 2]] = region[:, :, [2, 1]]

    return image

def main():
    if len(sys.argv) != 2:
        print("Usage: python glitchy_image_compressor.py <image_file>")
        sys.exit(1)

    input_path = sys.argv[1]

    # Check if file exists
    if not os.path.isfile(input_path):
        print(f"Error: File '{input_path}' does not exist.")
        sys.exit(1)

    # Read the image using OpenCV
    image = cv2.imread(input_path)
    if image is None:
        print(f"Error: Could not read image '{input_path}'")
        sys.exit(1)

    # Apply glitch effect
    glitched_image = add_glitch(image.copy())

    # Generate output filename
    base_name, ext = os.path.splitext(input_path)
    output_path = f"{base_name}_color_glitch.png"

    # Save the result
    cv2.imwrite(output_path, glitched_image)
    print(f"Glitched image saved as '{output_path}'")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from io import BytesIO
import numpy as np

# Original script code remains unchanged

def test_add_glitch():
    """Test the add_glitch function with a sample image."""
    # Create a sample image
    sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
    sample_image[50:, :] = [255, 0, 0]  # Blue region

    # Apply glitch
    glitched_image = add_glitch(sample_image.copy())

    # Check if the color channels have been swapped
    assert not np.array_equal(glitched_image[:50, :], sample_image[:50, :])
    assert not np.array_equal(glitched_image[50:, :], sample_image[50:, :])

def test_add_glitch_no_change():
    """Test the add_glitch function with an image where no glitch should occur."""
    # Create a sample image
    sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
    sample_image[50:, :] = [255, 0, 0]  # Blue region

    # Apply glitch with no change
    glitched_image = add_glitch(sample_image.copy(), glitch_probability=0)

    # Check if the image remains unchanged
    assert np.array_equal(glitched_image, sample_image)

def test_main_valid_input():
    """Test the main function with a valid input file."""
    # Create a sample image and save it to a BytesIO object
    sample_image = np.zeros((100, 100, 3), dtype=np.uint8)
    sample_image[50:, :] = [255, 0, 0]  # Blue region
    input_file = BytesIO()
    cv2.imwrite(input_file, sample_image)
    input_file.seek(0)

    # Call the main function with the sample image
    sys.argv = ["glitchy_image_compressor.py", input_file.name]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{input_file.name}_color_glitch.png"
    assert os.path.isfile(output_path)
    assert os.path.getsize(output_path) > 0

def test_main_invalid_input():
    """Test the main function with an invalid input file."""
    # Call the main function with a non-existent file
    sys.argv = ["glitchy_image_compressor.py", "non_existent_file.jpg"]
    with pytest.raises(SystemExit):
        main()

def test_main_invalid_arguments():
    """Test the main function with invalid arguments."""
    # Call the main function without any arguments
    sys.argv = ["glitchy_image_compressor.py"]
    with pytest.raises(SystemExit):
        main()
