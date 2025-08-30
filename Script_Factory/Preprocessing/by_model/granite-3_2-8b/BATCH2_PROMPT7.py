from PIL import Image
import random
import os

def glitch_image(image_path, output_path, error_rate=0.05):
    """
    Introduces pixel errors to an image for 'compression'.

    Args:
        image_path (str): Path to the input image file.
        output_path (str): Path to save the glitched image.
        error_rate (float): Probability of introducing a pixel error (default 0.05).
    """
    # Open the image using Pillow
    with Image.open(image_path) as img:
        width, height = img.size

        # Iterate through each pixel and introduce errors randomly
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))

                # Decide whether to introduce an error
                if random.random() < error_rate:
                    # Introduce a glitch by shifting the color values
                    img.putpixel((x, y), (
                        min(255, r + int(random.gauss(0, 10))),
                        min(255, g + int(random.gauss(0, 10))),
                        min(255, b + int(random.gauss(0, 10)))
                    ))

        # Save the glitched image
        img.save(output_path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: python BATCH2_PROMPT7_{model_name}.py <input_image> <output_image> <error_rate>")
        exit(1)

    input_image = sys.argv[1]
    output_image = sys.argv[2]
    error_rate_str = sys.argv[3]

    try:
        error_rate = float(error_rate_str)
    except ValueError:
        print("Error rate must be a number.")
        exit(1)

    glitch_image(input_image, output_image, error_rate)
    print(f"Glitching complete. Glitched image saved as {output_image}")