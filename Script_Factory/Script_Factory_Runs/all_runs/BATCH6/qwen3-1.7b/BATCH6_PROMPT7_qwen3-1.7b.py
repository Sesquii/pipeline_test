```python
import random
from PIL import Image
import sys

def main():
    # Check command line argument for input file path
    if len(sys.argv) != 2:
        print("Usage: python glitch_compressor.py <input_file>")
        return
    
    input_path = sys.argv[1]
    
    # Open the image file
    img = Image.open(input_path)
    width, height = img.size
    
    # Randomly decide how many pixels to corrupt (between 1 and 20)
    num_pixels = random.randint(1, 20)
    
    # Select a random number of pixels to corrupt
    corrupted_pixels = set()
    for _ in range(num_pixels):
        i = random.randint(0, width - 1)
        j = random.randint(0, height - 1)
        corrupted_pixels.add((i, j))
    
    # Apply corruption by setting RGB values to zero
    for i, j in corrupted_pixels:
        img.putpixel((i, j), (0, 0, 0))
    
    # Save the modified image with a new filename
    output_path = input_path.split('.')[0] + '_corrupt.jpg'
    img.save(output_path)
    print(f"Image saved as {output_path}")

if __name__ == "__main__":
    main()