from PIL import Image
import random

def glitchy_image_compressor(input_path):
    """
    Takes a PNG image and applies a "glitchy" dithering effect by reducing its color palette
    to 2-3 colors and randomly swapping pixels.

    Args:
        input_path (str): Path to the input PNG file.
    """

    # Open the original image
    img = Image.open(input_path)

    # Convert image to RGB mode if it's not already
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Reduce color palette to 2-3 colors using quantization
    reduced_img = img.quantize(colors=random.randint(2, 3))

    # Get the reduced palette
    palette = reduced_img.getpalette()

    if not palette:
        print("Error: Could not extract palette from image")
        return

    # Create a new image with the same size and mode as the original
    width, height = img.size
    output_img = Image.new('RGB', (width, height))

    # Process each pixel
    for y in range(height):
        for x in range(width):
            # Get the current pixel color from the reduced palette
            current_color = reduced_img.getpixel((x, y))
            
            # Get all possible colors in the palette
            colors_in_palette = set()
            for i in range(0, len(palette), 3):
                r, g, b = palette[i:i+3]
                colors_in_palette.add((r, g, b))

            # Remove the current color from possibilities to avoid swapping with itself
            colors_in_palette.discard(current_color)

            if not colors_in_palette:
                # If no other colors available, just use the current color
                output_img.putpixel((x, y), current_color)
            else:
                # Randomly choose a different color from the palette (with 50% chance)
                if random.random() < 0.5:
                    new_color = random.choice(list(colors_in_palette))
                    output_img.putpixel((x, y), new_color)
                else:
                    output_img.putpixel((x, y), current_color)

    # Save the processed image
    output_path = f"{input_path}_dithered.png"
    output_img.save(output_path)
    print(f"Processed image saved to: {output_path}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python glitchy_image_compressor.py <input_png_file>")
    else:
        input_file = sys.argv[1]
        glitchy_image_compressor(input_file)