from PIL import Image
import random

def corrupt_pixel(image):
    width, height = image.size
    pixels = image.load()

    for x in range(width):
        for y in range(height):
            if random.random() > 0.95:  # Adjust this probability to control the level of corruption
                r = max(0, random.randint(0, 255))
                g = max(0, random.randint(0, 255))
                b = max(0, random.randint(0, 255))
                pixels[x, y] = (r, g, b)

    return image

def glitch_compress(input_path, output_path):
    with Image.open(input_path) as img:
        corrupted_img = corrupt_pixel(img)
        corrupted_img.save(output_path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python glitchy_compressor.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = f"{input_path}_corrupt.jpg"

    glitch_compress(input_path, output_path)
    print(f"Glitchy compression completed. Output saved as {output_path}")