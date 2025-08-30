# Import necessary libraries
from PIL import Image, ImageDraw
import random

def dither_image(input_path):
    """
    Dithers an image by reducing its color palette to 2-3 colors and then swapping pixels.
    
    Args:
    input_path (str): The path to the PNG file to be dithered.
    
    Returns:
    None: Saves the dithered image as <input_filename>_dithered.png
    """
    # Open the image
    img = Image.open(input_path)
    
    # Convert the image to RGB mode
    img = img.convert("RGB")
    
    # Reduce color palette to 2-3 colors
    reduced_colors = []
    pixels = list(img.getdata())
    unique_pixels = set(pixels)
    
    for pixel in unique_pixels:
        if len(reduced_colors) < 2 and random.choice([True, False]):
            reduced_colors.append(pixel)
        elif len(reduced_colors) == 2 and not any(all(c1 == c2 for c1, c2 in zip(pixel, color)) for color in reduced_colors):
            if random.choice([True, False]):
                reduced_colors.append(pixel)
    
    # Create a new image with the reduced colors
    dithered_img = Image.new("RGB", img.size)
    draw = ImageDraw.Draw(dithered_img)
    
    for x in range(img.width):
        for y in range(img.height):
            pixel = pixels[y * img.width + x]
            closest_color = min(reduced_colors, key=lambda color: sum((c1 - c2) ** 2 for c1, c2 in zip(pixel, color)))
            draw.point((x, y), fill=closest_color)
    
    # Randomly swap pixels with a different color from the reduced palette
    for _ in range(10 * img.width * img.height):  # Number of swaps
        x1, y1 = random.randint(0, img.width - 1), random.randint(0, img.height - 1)
        pixel1 = pixels[y1 * img.width + x1]
        if pixel1 in reduced_colors:
            color_options = [color for color in reduced_colors if color != pixel1]
            new_color = random.choice(color_options) if color_options else pixel1
            pixels[y1 * img.width + x1] = new_color
    
    # Save the dithered image
    output_path = f"{input_path.split('.')[0]}_dithered.png"
    dithered_img.putdata(pixels)
    dithered_img.save(output_path)

# Entry point of the script
if __name__ == "__main__":
    input_path = "path_to_your_image.png"  # Replace with your image path
    dither_image(input_path)
```

This Python program uses the `Pillow` library to open and manipulate an image. It reduces the color palette of the image to 2-3 colors by randomly selecting unique pixels from the original image. Then, it swaps each pixel with a different color from the reduced palette. The dithered image is saved as `<input_filename>_dithered.png`.