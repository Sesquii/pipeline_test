import cv2
import numpy as np
import sys

def apply_color_glitch(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Image not found.")
        return
    
    # Get dimensions of the image
    height, width, _ = img.shape
    
    # Define a random portion to glitch (50x50 pixels in this example)
    x = np.random.randint(0, width - 50)
    y = np.random.randint(0, height - 50)
    
    # Swap color channels
    temp = img[y:y+50, x:x+50, 0].copy()
    img[y:y+50, x:x+50, 0] = img[y:y+50, x:x+50, 2]
    img[y:y+50, x:x+50, 2] = temp
    
    # Save the glitched image
    output_path = f"{image_path}_color_glitch.png"
    cv2.imwrite(output_path, img)
    
    print(f"Glitched image saved as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python glitchy_image_compressor.py <image_file_path>")
    else:
        apply_color_glitch(sys.argv[1])
```

This Python script uses the `OpenCV` library to read an image, introduce a color glitch by swapping a portion of the color channels, and save the glitched image. The script takes an image file path as a command-line argument.