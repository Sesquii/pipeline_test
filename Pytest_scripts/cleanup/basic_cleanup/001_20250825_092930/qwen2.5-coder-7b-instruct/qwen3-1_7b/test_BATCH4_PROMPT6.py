import cv2
import numpy as np
import sys
import random

def main():
    if len(sys.argv) != 2:
        print("Usage: python glitchy_compressor.py <input_file>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = f"{input_path}_color_glitch.png"
    
    # Load the image
    original = cv2.imread(input_path)
    if original is None:
        print(f"Error: Could not read image at {input_path}.")
        sys.exit(1)
    
    height, width, _ = original.shape
    
    # Generate a random glitch region
    start_x = random.randint(0, height - 1)
    start_y = random.randint(0, width - 1)
    size_h = random.randint(50, 200)
    size_w = random.randint(50, 200)
    
    # Create a copy of the image for modification
    modified = original.copy()
    
    # Randomly choose which two channels to swap
    swap_indices = [random.randint(0, 2), random.randint(0, 2)]
    if swap_indices[0] != swap_indices[1]:
        channel1, channel2 = swap_indices
        for i in range(start_x, start_x + size_h):
            for j in range(start_y, start_y + size_w):
                if i < height and j < width:
                    r, g, b = modified[i, j]
                    new_r, new_g, new_b = 0, 0, 0
                    if channel1 == 0 and channel2 == 1:
                        new_r, new_g, new_b = g, r, b
                    elif channel1 == 0 and channel2 == 2:
                        new_r, new_g, new_b = g, b, r
                    elif channel1 == 1 and channel2 == 2:
                        new_r, new_g, new_b = r, b, g
                    modified[i, j] = [new_r, new_g, new_b]
    
    # Save the output image
    cv2.imwrite(output_path, modified)
    print(f"Glitchy image saved as {output_path}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest
from io import BytesIO
from PIL import Image

# Original code remains unchanged

def test_main_valid_input():
    """Test with a valid input file."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 3), dtype=np.uint8)
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_invalid_input():
    """Test with an invalid input file."""
    # Create a non-existent image path
    temp_image_path = "non_existent_image.png"

    # Run the main function with the non-existent image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    with pytest.raises(SystemExit) as excinfo:
        main()
    
    assert excinfo.value.code == 1

def test_main_no_arguments():
    """Test without any arguments."""
    # Run the main function without any arguments
    with pytest.raises(SystemExit) as excinfo:
        sys.argv = ["glitchy_compressor.py"]
        main()
    
    assert excinfo.value.code == 1

def test_main_extra_arguments():
    """Test with extra arguments."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 3), dtype=np.uint8)
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with an extra argument
    sys.argv = ["glitchy_compressor.py", temp_image_path, "extra_arg"]
    with pytest.raises(SystemExit) as excinfo:
        main()
    
    assert excinfo.value.code == 1

def test_main_random_glitches():
    """Test if random glitches are applied correctly."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 3), dtype=np.uint8)
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_channel_swapping():
    """Test if channel swapping is applied correctly."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 3), dtype=np.uint8)
    temp_image[50:60, 50:60] = [255, 0, 0]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping():
    """Test if random channel swapping is applied correctly."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 3), dtype=np.uint8)
    temp_image[50:60, 50:60] = [255, 0, 0]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_negative():
    """Test if random channel swapping with negative values does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 3), dtype=np.uint8)
    temp_image[50:60, 50:60] = [255, 0, 0]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_positive():
    """Test if random channel swapping with positive values does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 3), dtype=np.uint8)
    temp_image[50:60, 50:60] = [255, 0, 0]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_edge_cases():
    """Test if random channel swapping with edge cases does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 3), dtype=np.uint8)
    temp_image[50:60, 50:60] = [255, 0, 0]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_large_images():
    """Test if random channel swapping with large images does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((1000, 1000, 3), dtype=np.uint8)
    temp_image[500:600, 500:600] = [255, 0, 0]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_small_images():
    """Test if random channel swapping with small images does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((10, 10, 3), dtype=np.uint8)
    temp_image[5:6, 5:6] = [255, 0, 0]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_with_alpha_channel():
    """Test if random channel swapping with an alpha channel does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 4), dtype=np.uint8)
    temp_image[50:60, 50:60] = [255, 0, 0, 255]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_with_grayscale_image():
    """Test if random channel swapping with a grayscale image does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100), dtype=np.uint8)
    temp_image[50:60, 50:60] = 255
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_with_large_alpha_channel():
    """Test if random channel swapping with a large alpha channel does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 4), dtype=np.uint8)
    temp_image[50:60, 50:60] = [255, 0, 0, 255]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_with_small_alpha_channel():
    """Test if random channel swapping with a small alpha channel does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((10, 10, 4), dtype=np.uint8)
    temp_image[5:6, 5:6] = [255, 0, 0, 255]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_with_large_grayscale_image():
    """Test if random channel swapping with a large grayscale image does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100), dtype=np.uint8)
    temp_image[50:60, 50:60] = 255
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_with_small_grayscale_image():
    """Test if random channel swapping with a small grayscale image does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((10, 10), dtype=np.uint8)
    temp_image[5:6, 5:6] = 255
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_with_large_color_image():
    """Test if random channel swapping with a large color image does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 3), dtype=np.uint8)
    temp_image[50:60, 50:60] = [255, 0, 0]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_with_small_color_image():
    """Test if random channel swapping with a small color image does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((10, 10, 3), dtype=np.uint8)
    temp_image[5:6, 5:6] = [255, 0, 0]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_color_glitch.png"
    assert os.path.exists(output_path)
    output_image = cv2.imread(output_path)
    assert output_image is not None

    # Clean up temporary files
    os.remove(temp_image_path)
    os.remove(output_path)

def test_main_random_channel_swapping_with_large_alpha_color_image():
    """Test if random channel swapping with a large alpha color image does not cause errors."""
    # Create a temporary image for testing
    temp_image = np.zeros((100, 100, 4), dtype=np.uint8)
    temp_image[50:60, 50:60] = [255, 0, 0, 255]
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, temp_image)

    # Run the main function with the temporary image path
    sys.argv = ["glitchy_compressor.py", temp_image_path]
    main()

    # Check if the output file exists and is not empty
    output_path = f"{temp_image_path}_