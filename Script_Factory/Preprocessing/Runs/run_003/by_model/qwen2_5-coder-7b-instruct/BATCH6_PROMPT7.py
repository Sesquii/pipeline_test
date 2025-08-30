from PIL import Image
import random

def glitchy_image_compressor(input_path):
    # Open the input image
    with Image.open(input_path) as img:
        width, height = img.size
        
        # Get a random number of pixels to corrupt (up to 10% of the total pixels)
        num_pixels_to_corrupt = random.randint(0, int(width * height * 0.1))
        
        # Loop through each pixel and randomly set its RGB values to 0
        for _ in range(num_pixels_to_corrupt):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            img.putpixel((x, y), (0, 0, 0))
        
        # Save the corrupted image with a new filename
        output_filename = f"{input_path.split('.')[0]}_corrupt.jpg"
        img.save(output_filename)

# Entry point of the program
if __name__ == "__main__":
    input_image_path = "path_to_your_image.jpg"  # Replace with your JPG file path
    glitchy_image_compressor(input_image_path)
```

Replace `"path_to_your_image.jpg"` with the actual path to your JPG image file. This script will open the specified image, randomly corrupt a number of pixels by setting their RGB values to 0, and save the corrupted image with a new filename in the same directory as the original.