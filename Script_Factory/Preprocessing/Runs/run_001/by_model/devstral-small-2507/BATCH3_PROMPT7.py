# BATCH3_PROMPT7_Devstral.py

from PIL import Image
import random

def add_random_artifacts(image, artifact_probability=0.01):
    """
    Introduce random pixel artifacts in an image.

    Args:
        image (Image): The input PIL Image object.
        artifact_probability (float): Probability of altering a pixel (default: 0.01).

    Returns:
        Image: The modified image with random artifacts.
    """
    pixels = image.load()  # Load pixel data
    width, height = image.size

    for y in range(height):
        for x in range(width):
            if random.random() < artifact_probability:
                # Introduce random color changes to selected pixels
                r, g, b = pixels[x, y]
                new_r = min(255, max(0, r + random.randint(-30, 30)))
                new_g = min(255, max(0, g + random.randint(-30, 30)))  
                new_b = min(255, max(0, b + random.randint(-30, 30)))
                pixels[x, y] = (new_r, new_g, new_b)

    return image

def glitchy_compress(input_path, output_path, artifact_probability=0.01):
    """
    Compress an image by adding random artifacts.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the compressed image.
        artifact_probability (float): Probability of altering a pixel (default: 0.01).
    """
    try:
        with Image.open(input_path) as img:
            modified_img = add_random_artifacts(img, artifact_probability)
            modified_img.save(output_path, optimize=True, quality=85)
            print(f"Image saved to {output_path} with glitchy compression applied.")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    # Example usage
    input_image = "input.jpg"
    output_image = "glitchy_compressed.jpg"

    try:
        glitchy_compress(input_image, output_image, artifact_probability=0.02)
    except Exception as e:
        print(f"Error: {e}")