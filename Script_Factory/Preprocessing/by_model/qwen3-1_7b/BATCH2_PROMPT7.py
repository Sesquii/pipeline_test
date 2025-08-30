```python
import random
from PIL import Image

def compress_image(input_path, output_path, percentage=0.1):
    """
    Compresses an image by introducing random pixel errors or artifacts.
    
    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path where the compressed image will be saved.
        percentage (float): Percentage of pixels to modify for glitch effects.
            Default is 0.1 (10%).
    """
    # Load the input image
    img = Image.open(input_path)
    width, height = img.size
    
    # Calculate how many pixels to change
    num_pixels = width * height
    change_count = int(num_pixels * percentage)
    
    # Create a new image with same size
    new_img = Image.new('RGB', (width, height))
    
    # Generate random colors for the changes
    for i in range(change_count):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        new_img.putpixel((x, y), (r, g, b))
    
    # Save the compressed image
    new_img.save(output_path, 'PNG')

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python BATCH2_PROMPT7_{{model_name}}.py input_image output_image")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    compress_image(input_path, output_path)