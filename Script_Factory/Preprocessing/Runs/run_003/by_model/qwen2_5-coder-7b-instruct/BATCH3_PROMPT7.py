#!/usr/bin/env python3

import os
from PIL import Image
import random

def glitch_image(input_path, output_path):
    # Open the image using Pillow
    with Image.open(input_path) as img:
        width, height = img.size
        
        # Convert image to RGB mode if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Create a new image to hold the glitched version
        glitch_img = img.copy()
        
        # Introduce pixel errors randomly
        for x in range(width):
            for y in range(height):
                if random.random() < 0.1:  # 10% chance to glitch a pixel
                    glitch_img.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        
        # Save the glitched image
        glitch_img.save(output_path)

if __name__ == "__main__":
    input_image = 'input.jpg'  # Replace with your input image path
    output_image = 'output_glitched.jpg'  # Replace with desired output path
    
    if not os.path.exists(input_image):
        print(f"Error: Input file {input_image} does not exist.")
    else:
        glitch_image(input_image, output_image)
        print(f"Glitchy image saved as {output_image}")
```

This Python script uses the Pillow library to open an image and introduces random pixel errors (artifacts) to simulate a "glitched" effect. The probability of introducing an error is 10%. The glitched image is then saved to the specified output path.