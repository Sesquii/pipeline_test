import cv2
import sys
import random
import numpy as np

def glitch_image(image_path):
    # Load image using OpenCV
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Error loading image from {image_path}")
        return

    height, width, channels = img.shape

    # Choose a random region to glitch
    x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
    x2, y2 = random.randint(x1 + 1, min(width, x1 + 64)), random.randint(y1 + 1, min(height, y1 + 64))

    # Swap color channels within the chosen region
    for i in range(x1, x2):
        for j in range(y1, y2):
            temp = img[j, i].copy()
            img[j, i] = temp[2], temp[1], temp[0]  # Swap BGR to RGB (common in OpenCV)

    # Save the glitch image
    output_filename = f"{image_path.split('/')[-1]}_color_glitch.png"
    cv2.imwrite(output_filename, img)
    print(f"Glitch applied and saved as {output_filename}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python glitchy_compressor.py <image_file>")
        return

    image_path = sys.argv[1]
    glitch_image(image_path)

if __name__ == "__main__":
    main()