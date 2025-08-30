import random
from PIL import Image

def glitch_image(image_path, output_path):
    """
    Glitches an image by randomly introducing pixel errors.

    Parameters:
    - image_path: Path to the input image file.
    - output_path: Path to save the glitched image file.
    """
    # Open the image
    with Image.open(image_path) as img:
        pixels = img.load()
        width, height = img.size

        # Randomly introduce pixel errors
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                glitch_r = (r + random.randint(-50, 50)) % 256
                glitch_g = (g + random.randint(-50, 50)) % 256
                glitch_b = (b + random.randint(-50, 50)) % 256
                pixels[x, y] = (glitch_r, glitch_g, glitch_b)

        # Save the glitched image
        img.save(output_path)

if __name__ == "__main__":
    input_image_path = "input.jpg"  # Replace with your input image path
    output_image_path = "output_glitched.jpg"  # Replace with your desired output file path
    glitch_image(input_image_path, output_image_path)
```

This Python script uses the Pillow library to open an image and introduce random pixel errors by modifying the RGB values of each pixel. The modified image is then saved to a specified output file.