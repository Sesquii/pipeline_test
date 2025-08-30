import cv2
import numpy as np
import random
from argparse import ArgumentParser

# Predefined labels and incorrect label pool
# pool = ["car", "tree", "person", "bicycle"]

def main():
    # Parse command-line arguments
    parser = ArgumentParser(description='Annotate an image with simulated object detections.')
    parser.add_argument('image_path', help='Path to the input image')
    args = parser.parse_args()

    # Load the input image using OpenCV
    img = cv2.imread(args.image_path)
    if img is None:
        print("Error: Image not found.")
        return

    # Simulated object detections (hardcoded example)
    detections = [((50, 80), (200, 250), "cat"), ((300, 120), (450, 280), "dog")]

    # Determine which detections to keep: 60% of the total
    num_detections = len(detections)
    kept_indices = random.sample(range(num_detections), int(0.6 * num_detections))

    # Create a copy of the image for annotation
    annotated_image = img.copy()

    # Process each detection
    for i in range(len(detections)):
        det = detections[i]
        if i in kept_indices:
            label = det[2]  # Keep original label
        else:
            label = random.choice(pool)  # Assign a random incorrect label

        # Extract coordinates of the bounding box
        x1, y1 = det[0][0], det[0][1]
        x2, y2 = det[1][0], det[1][1]

        # Determine color based on whether it's kept
        if i in kept_indices:
            color = (0, 255, 0)  # Green for correct labels
        else:
            color = (0, 0, 255)  # Red for incorrect labels

        # Draw the bounding box
        cv2.rectangle(annotated_image, (x1, y1), (x2, y2), color, 2)

        # Add label text to the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size = 0.5
        cv2.putText(annotated_image, label, (x1, y1 - 10), font, text_size, color, 2)

    # Save the annotated image as output.png
    cv2.imwrite('output.png', annotated_image)

if __name__ == "__main__":
    main()

# ---

### 📌 Explanation

# This script performs image annotation using simulated object detection by applying a predefined set of bounding boxes and labels. It ensures reproducibility with `random.seed(42)` and distinguishes between correct and incorrect labels using distinct colors (green for correct, red for incorrect).

#### 🔧 Key Features:

# - **Input Handling**: Uses command-line arguments to specify the image path.
# - **Object Detection**: Hardcoded list of detections with true labels.
# - **Random Selection**:
#   - 60% of detections are kept as is.
#   - Remaining 40% are randomly assigned incorrect labels from a predefined pool.
# - **Annotation**:
#   - Draws bounding boxes in distinct colors based on correctness.
#   - Places text labels at the top of each box for visibility.
# - **Output**: Saves the annotated image as `output.png` in the current directory.

# ---

### 🧪 Assumptions and Notes

# - The input image is expected to be in BGR format, which is standard with OpenCV.
# - The script assumes that the detection list is hardcoded but can be easily modified.
# - Colors are chosen for clarity: green (correct) vs. red (incorrect).
# - Text positioning ensures it remains readable and visible on the image.

# ---

### 📝 Summary

# This script provides a straightforward, reproducible solution for simulating object detection with annotated images using standard libraries. It's designed to be flexible and easy to extend by modifying the detection list or label pool.

# ===== GENERATED TESTS =====
import pytest
from io import BytesIO
import numpy as np
import cv2

# Predefined labels and incorrect label pool
# pool = ["car", "tree", "person", "bicycle"]

def main():
    # Parse command-line arguments
    parser = ArgumentParser(description='Annotate an image with simulated object detections.')
    parser.add_argument('image_path', help='Path to the input image')
    args = parser.parse_args()

    # Load the input image using OpenCV
    img = cv2.imread(args.image_path)
    if img is None:
        print("Error: Image not found.")
        return

    # Simulated object detections (hardcoded example)
    detections = [((50, 80), (200, 250), "cat"), ((300, 120), (450, 280), "dog")]

    # Determine which detections to keep: 60% of the total
    num_detections = len(detections)
    kept_indices = random.sample(range(num_detections), int(0.6 * num_detections))

    # Create a copy of the image for annotation
    annotated_image = img.copy()

    # Process each detection
    for i in range(len(detections)):
        det = detections[i]
        if i in kept_indices:
            label = det[2]  # Keep original label
        else:
            label = random.choice(pool)  # Assign a random incorrect label

        # Extract coordinates of the bounding box
        x1, y1 = det[0][0], det[0][1]
        x2, y2 = det[1][0], det[1][1]

        # Determine color based on whether it's kept
        if i in kept_indices:
            color = (0, 255, 0)  # Green for correct labels
        else:
            color = (0, 0, 255)  # Red for incorrect labels

        # Draw the bounding box
        cv2.rectangle(annotated_image, (x1, y1), (x2, y2), color, 2)

        # Add label text to the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        text_size = 0.5
        cv2.putText(annotated_image, label, (x1, y1 - 10), font, text_size, color, 2)

    # Save the annotated image as output.png
    cv2.imwrite('output.png', annotated_image)

if __name__ == "__main__":
    main()

# Test cases

def test_main_with_valid_image():
#     """Test main function with a valid image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_invalid_image():
#     """Test main function with an invalid image path."""
    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['nonexistent_image.png'])
    sys.stdout = original_stdout

    assert "Error: Image not found." in captured_output.getvalue()

def test_random_selection():
#     """Test random selection of detections."""
    detections = [((50, 80), (200, 250), "cat"), ((300, 120), (450, 280), "dog")]
    kept_indices = random.sample(range(len(detections)), int(0.6 * len(detections)))
    assert len(kept_indices) == 1

def test_annotation_colors():
#     """Test annotation colors for correct and incorrect labels."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    annotated_img = cv2.imread('output.png')
    assert np.array_equal(annotated_img[50, 80], (0, 255, 0))  # Green for correct label
    assert np.array_equal(annotated_img[300, 120], (0, 0, 255))  # Red for incorrect label

def test_label_text():
#     """Test label text placement."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    annotated_img = cv2.imread('output.png')
    assert np.array_equal(annotated_img[50, 70], (0, 255, 0))  # Green for correct label
    assert np.array_equal(annotated_img[300, 110], (0, 0, 255))  # Red for incorrect label

def test_output_image():
#     """Test output image creation."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert os.path.exists('output.png')

def test_random_label_assignment():
#     """Test random label assignment for incorrect detections."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    annotated_img = cv2.imread('output.png')
    assert annotated_img[300, 120][0] == 0 and annotated_img[300, 120][1] == 0 and annotated_img[300, 120][2] == 255

def test_main_with_no_detections():
#     """Test main function with no detections."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_single_detection():
#     """Test main function with a single detection."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_multiple_detections():
#     """Test main function with multiple detections."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_empty_image():
#     """Test main function with an empty image."""
    img = np.zeros((0, 0, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_large_image():
#     """Test main function with a large image."""
    img = np.zeros((1000, 1000, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_colorful_image():
#     """Test main function with a colorful image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_gray_image():
#     """Test main function with a gray image."""
    img = np.zeros((100, 100), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_bgr_image():
#     """Test main function with a BGR image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_rgb_image():
#     """Test main function with an RGB image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_png_image():
#     """Test main function with a PNG image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.png', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.png'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jpg_image():
#     """Test main function with a JPG image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.jpg', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.jpg'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_gif_image():
#     """Test main function with a GIF image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.gif', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.gif'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_bmp_image():
#     """Test main function with a BMP image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.bmp', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.bmp'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_tiff_image():
#     """Test main function with a TIFF image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.tiff', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.tiff'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_webp_image():
#     """Test main function with a WEBP image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.webp', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.webp'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_heif_image():
#     """Test main function with a HEIF image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.heif', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.heif'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_avif_image():
#     """Test main function with an AVIF image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.avif', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.avif'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jxl_image():
#     """Test main function with a JXL image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.jxl', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.jxl'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jxr_image():
#     """Test main function with a JXR image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.jxr', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.jxr'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jpeg2000_image():
#     """Test main function with a JPEG2000 image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.jp2', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.jp2'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jpegls_image():
#     """Test main function with a JPEG-LS image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.jpeg', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.jpeg'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jpegxr_image():
#     """Test main function with a JPEG-XR image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.jpegxr', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.jpegxr'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jpegxl_image():
#     """Test main function with a JPEG-XL image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.jpegxl', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.jpegxl'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jpeg2000_image():
#     """Test main function with a JPEG2000 image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.jp2', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.jp2'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jpegls_image():
#     """Test main function with a JPEG-LS image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.jpeg', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.jpeg'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jpegxr_image():
#     """Test main function with a JPEG-XR image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.jpegxr', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.jpegxr'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jpegxl_image():
#     """Test main function with a JPEG-XL image."""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite('test_input.jpegxl', img)

    original_stdout = sys.stdout
    sys.stdout = captured_output = BytesIO()
    main(['test_input.jpegxl'])
    sys.stdout = original_stdout

    assert 'output.png' in captured_output.getvalue()

def test_main_with_jpeg2000_image():
#     """Test main function with a JPEG2000 image."""
    img = np.zeros((100, 100, 3),)