import argparse
import random
from PIL import Image

def ascii_art(image_path, max_width=100):
    # Open and convert image to grayscale
    img = Image.open(image_path).convert('L')
    
    # Calculate new dimensions while preserving aspect ratio
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(max_width * aspect_ratio)
    img = img.resize((max_width, new_height))
    
    # Map pixel intensities to ASCII characters
    ascii_set = "@%#*+=-:. "
    pixels = list(img.getdata())
    ascii_string = "".join(ascii_set[pixel // 25] for pixel in pixels)
    
    # Corrupt exactly 10% of the characters randomly
    random.seed(42)
    total_chars = len(ascii_string)
    num_corrupted = int(total_chars * 0.1)
    indices_to_corrupt = random.sample(range(total_chars), num_corrupted)
    corrupted_ascii_string = ''.join(
        ascii_set[random.randint(0, len(ascii_set)-1)] if i in indices_to_corrupt else char
        for i, char in enumerate(ascii_string)
    )
    
    return corrupted_ascii_string

def main():
    parser = argparse.ArgumentParser(description="Glitchy ASCII Artist")
    parser.add_argument("--input", required=True, help="Path to the input image file.")
    parser.add_argument("--width", type=int, default=100, help="Maximum width of the ASCII art in characters (default is 100).")
    parser.add_argument("--output", default="output.txt", help="Output file for the ASCII art (default is output.txt).")
    
    args = parser.parse_args()
    
    try:
        ascii_art_str = ascii_art(args.input, args.width)
        print(ascii_art_str)
        with open(args.output, 'w') as f:
            f.write(ascii_art_str)
        print(f"Glitchy ASCII art saved to {args.output}")
    except FileNotFoundError:
        print("Error: The input file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

This script reads an image, converts it to grayscale, scales it to a specified width while preserving the aspect ratio, maps pixel intensities to ASCII characters, corrupts 10% of these characters randomly, and prints the final glitchy ASCII art to stdout as well as saving it to a file. The script includes error handling for missing files and invalid arguments.