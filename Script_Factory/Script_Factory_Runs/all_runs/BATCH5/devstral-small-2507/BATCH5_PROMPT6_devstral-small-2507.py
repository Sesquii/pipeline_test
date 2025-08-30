import cv2
import numpy as np
import sys
import os

def add_color_glitch(image):
    # Get image dimensions
    height, width, channels = image.shape

    # Determine the size of the glitch area (10% of the image)
    glitch_size = min(height, width) // 10

    # Randomly select a starting point for the glitch
    start_x = np.random.randint(0, width - glitch_size)
    start_y = np.random.randint(0, height - glitch_size)

    # Create a mask for the glitch area
    mask = np.zeros((height, width), dtype=np.bool_)
    mask[start_y:start_y+glitch_size, start_x:start_x+glitch_size] = True

    # Get the color channels
    b, g, r = cv2.split(image)

    # Randomly swap two channels within the glitch area
    if np.random.rand() > 0.5:
        # Swap blue and green
        b_masked = np.where(mask, g, b)
        g_masked = np.where(mask, b, g)
        r_masked = r
    else:
        # Swap green and red  
        g_masked = np.where(mask, r, g)
        r_masked = np.where(mask, g, r)
        b_masked = b

    # Merge the channels back together
    glitched_image = cv2.merge((b_masked, g_masked, r_masked))

    return glitched_image

def main():
    if len(sys.argv) != 2:
        print("Usage: python glitchy_image_compressor.py <image_path>")
        sys.exit(1)

    input_path = sys.argv[1]

    # Read the input image
    try:
        image = cv2.imread(input_path)
        if image is None:
            raise FileNotFoundError(f"Cannot read image file: {input_path}")
    except Exception as e:
        print(f"Error reading image: {e}")
        sys.exit(1)

    # Add color glitch to the image
    glitched_image = add_color_glitch(image)

    # Generate output filename
    input_dir = os.path.dirname(input_path)
    input_filename = os.path.basename(input_path)
    name_part, ext_part = os.path.splitext(input_filename)
    output_filename = f"{name_part}_color_glitch{ext_part}"
    output_path = os.path.join(input_dir, output_filename)

    # Save the glitched image
    try:
        cv2.imwrite(output_path, glitched_image)
        print(f"Glitched image saved to: {output_path}")
    except Exception as e:
        print(f"Error saving image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()