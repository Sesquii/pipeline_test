# BATCH3_PROMPT7_Granite.py

import random
from PIL import Image

def glitch_image(image_path: str, output_path: str, error_rate: float = 0.1) -> None:
    """
    Glitch an image by randomly introducing pixel errors or artifacts.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the glitched image.
        error_rate (float, optional): Probability of a pixel being affected by the glitch. Defaults to 0.1.
    """
    # Open the image using Pillow's Image module
    img = Image.open(image_path)
    
    width, height = img.size

    # Iterate over each pixel in the image
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))

            # Randomly introduce a glitch with given error rate
            if random.random() < error_rate:
                # Introduce random errors to RGB values
                r += random.randint(-10, 10)
                g += random.randint(-10, 10)
                b += random.randint(-10, 10)

                # Ensure the RGB values stay within valid range (0-255)
                r = max(0, min(255, r))
                g = max(0, min(255, g))
                b = max(0, min(255, b))

            # Set the pixel to the new RGB value
            img.putpixel((x, y), (r, g, b))

    # Save the glitch-ed image
    img.save(output_path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python BATCH3_PROMPT7_Granite.py <input_image> <output_image> <error_rate>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    try:
        error_rate = float(sys.argv[3])
    except ValueError:
        print("Error rate must be a floating point number.")
        sys.exit(1)

    glitch_image(input_path, output_path, error_rate)
    print(f"Glitched image saved to {output_path}")