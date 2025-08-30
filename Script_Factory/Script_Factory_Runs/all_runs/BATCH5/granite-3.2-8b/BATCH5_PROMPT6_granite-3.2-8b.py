import cv2
import sys
import numpy as np
import random

def glitch_image(input_path):
    # Load image using OpenCV
    img = cv2.imread(input_path)

    if img is None:
        print(f"Error: Could not read {input_path}")
        return

    # Get image dimensions
    height, width, _ = img.shape

    # Randomly select a portion of the image to glitch (between 10% and 20% of the total area)
    glitch_area = random.randint(int(height * width * 0.1), int(height * width * 0.2))
    x1, y1 = random.randint(0, height - 50), random.randint(0, width - 50)  # Avoid borders
    x2, y2 = x1 + random.randint(10, 30), y1 + random.randint(10, 30)

    # Extract the portion to glitch
    glitch_portion = img[y1:y2, x1:x2]

    # Flatten the glitch portion and shuffle its color channels
    flat_glitch = glitch_portion.reshape(-1, 3)
    np.random.shuffle(flat_glitch)

    # Restore to original shape but with shuffled channels
    glitch_portion = flat_glitch.reshape((y2 - y1, x2 - x1, 3))

    # Replace the selected portion in the original image with the glitched one
    img[y1:y2, x1:x2] = glitch_portion

    # Save the glitched image
    output_path = f"{input_path.split('/')[-1].rsplit('.', 1)[0]}_color_glitch.png"
    cv2.imwrite(output_path, img)
    print(f"Glitched image saved as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python glitchy_image_compressor.py <path_to_image>")
    else:
        glitch_image(sys.argv[1])