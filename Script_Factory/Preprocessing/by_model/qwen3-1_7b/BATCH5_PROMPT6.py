```python
import sys
import random
import cv2
import numpy as np

def main():
    if len(sys.argv) != 2:
        print("Usage: python glitch_compressor.py <input_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = f"{input_filename}_color_glitch.png"

    # Load the image
    img = cv2.imread(input_filename)
    if img is None:
        print(f"Error: Could not load image {input_filename}")
        sys.exit(1)

    height, width, channels = img.shape
    if channels != 3:
        print("Error: Image must have 3 channels (RGB)")
        sys.exit(1)

    # Generate random region
    x_start = random.randint(0, height - 1)
    y_start = random.randint(0, width - 1)
    size_x = random.randint(50, 200)
    size_y = random.randint(50, 200)

    # Ensure the region is within bounds
    x_end = x_start + size_x
    y_end = y_start + size_y

    if x_end > height or y_end > width:
        print("Error: Region out of image boundaries")
        sys.exit(1)

    # Create a copy of the image to modify
    modified_img = np.copy(img)
    
    # Generate swap options (B-R, B-G, R-G)
    swap_options = [(0, 2), (0, 1), (1, 2)]

    # Apply swaps to the region
    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            b, g, r = modified_img[i, j]
            swap_idx = random.choice(swap_options)
            if swap_idx == (0, 2):  # Swap B and R
                new_b, new_g, new_r = r, g, b
            elif swap_idx == (0, 1):  # Swap B and G
                new_b, new_g, new_r = b, r, g
            elif swap_idx == (1, 2):  # Swap G and R
                new_b, new_g, new_r = b, r, g

            modified_img[i, j] = [new_b, new_g, new_r]

    # Save the output
    cv2.imwrite(output_filename, modified_img)
    print(f"Image saved as {output_filename}")

if __name__ == "__main__":
    main()