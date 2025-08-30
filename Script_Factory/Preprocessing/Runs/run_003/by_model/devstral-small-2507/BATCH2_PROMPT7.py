# BATCH2_PROMPT7_Devstral.py

from PIL import Image
import random

def glitch_image(input_path, output_path, glitch_percentage=5):
    """
    Introduce random pixel errors to reduce image file size.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the glitched image.
        glitch_percentage (float): Percentage of pixels to glitch (0-100).
    """
    try:
        # Open the original image
        with Image.open(input_path) as img:
            # Convert to RGB if not already
            img = img.convert('RGB')
            
            # Get image dimensions
            width, height = img.size
            total_pixels = width * height
            
            # Calculate number of pixels to glitch
            num_glitches = int(total_pixels * (glitch_percentage / 100.0))
            
            # Create a copy to modify
            glitched_img = img.copy()
            pixels = glitched_img.load()
            
            # Randomly select pixels to glitch
            for _ in range(num_glitches):
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                
                # Replace with random color
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                pixels[x, y] = (r, g, b)
            
            # Save the glitched image
            glitched_img.save(output_path)
            print(f"Glitched image saved to {output_path}")
    
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Glitchy Image Compressor")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("output", help="Output glitched image file path")
    parser.add_argument("--glitch", type=float, default=5, help="Percentage of pixels to glitch (0-100)")

    args = parser.parse_args()

    # Run the glitching process
    glitch_image(args.input, args.output, args.glitch)