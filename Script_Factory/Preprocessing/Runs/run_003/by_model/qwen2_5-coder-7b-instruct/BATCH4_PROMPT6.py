import cv2
import numpy as np
import sys

def glitch_image(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Unable to load image.")
        return
    
    # Get image dimensions
    height, width, channels = img.shape
    
    # Define the portion of the image to glitch (e.g., 10% of the image in each dimension)
    glitch_height = int(height * 0.1)
    glitch_width = int(width * 0.1)
    
    # Calculate starting points for the glitch
    start_y = np.random.randint(0, height - glitch_height)
    start_x = np.random.randint(0, width - glitch_width)
    
    # Define the portion to swap
    glitch_portion = img[start_y:start_y+glitch_height, start_x:start_x+glitch_width]
    
    # Randomly shuffle the channels
    for i in range(channels):
        np.random.shuffle(glitch_portion[:, :, i])
    
    # Replace the original portion with the glitched one
    img[start_y:start_y+glitch_height, start_x:start_x+glitch_width] = glitch_portion
    
    # Save the glitched image
    output_path = f"{image_path.split('.')[0]}_color_glitch.png"
    cv2.imwrite(output_path, img)
    
    print(f"Glitched image saved as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python glitch_image.py <image_file_path>")
    else:
        glitch_image(sys.argv[1])
```

This Python script uses the `OpenCV` library to load and modify an image. It introduces a glitch by randomly swapping a portion of the color channels. The output is saved as `<input_filename>_color_glitch.png`.