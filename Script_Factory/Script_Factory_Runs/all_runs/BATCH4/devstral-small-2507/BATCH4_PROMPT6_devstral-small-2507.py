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