#!/usr/bin/env python3
import sys
from PIL import Image
import argparse
import random

# Define ASCII character set
ASCII_SET = "@%#*+=-:. "

def img_to_ascii(img_path, max_width=None):
    """Convert an image to ASCII art."""

    # Open the image file
    try:
        with Image.open(img_path) as img:
            width, height = img.size

            # Resize if max_width is provided
            if max_width:
                ratio = min(max_width / width, height / max_width)
                new_width = int(width * ratio)
                new_height = int(height * ratio)
                img = img.resize((new_width, new_height), Image.ANTIALIAS)

            # Calculate the scale factor
            scale = max(1, min(img.size[0] / len(ASCII_SET), img.size[1] / (len(ASCII_SET) * ratio)))

            # Downscale image for better ASCII representation
            img = img.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)

            # Convert to grayscale and get pixel data
            pixels = img.convert('L').getdata()

    except FileNotFoundError:
        print("Error: The specified file does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    return pixels, scale

def pixel_to_ascii(pixels, scale):
    """Map pixel intensities to ASCII characters."""
    ascii_string = ''
    for pixel in pixels:
        intensity = int(pixel / 255 * len(ASCII_SET))
        ascii_string += ASCII_SET[intensity]

    return ascii_string

def add_glitches(ascii_string, seed=42):
    """Randomly corrupt a percentage of characters."""
    random.seed(seed)
    corrupted = 0
    glitchy_ascii = list(ascii_string)

    for i in range(len(glitchy_ascii)):
        if random.random() < 0.1 and corrupted < 10:  # Corrupt 10% of characters
            new_char = random.choice(ASCII_SET) if glitchy_ascii[i] != ' ' else ' '
            glitchy_ascii[i] = new_char
            corrupted += 1

    return ''.join(glitchy_ascii)

def main():
    parser = argparse.ArgumentParser(description='Glitchy ASCII Art Generator')
    parser.add_argument('--input', '-i', required=True, help='Path to the input image file')
    parser.add_argument('--width', '-w', type=int, help='Maximum width of the output in characters')

    args = parser.parse_args()

    pixels, scale = img_to_ascii(args.input, args.width)
    ascii_string = pixel_to_ascii(pixels, scale)
    glitchy_ascii = add_glitches(ascii_string)

    print(glitchy_ascii)

    output_file = 'output.txt'
    with open(output_file, 'w') as f:
        f.write(glitchy_ascii)

    print(f"Glitchy ASCII art saved to {output_file}")

if __name__ == '__main__':
    main()