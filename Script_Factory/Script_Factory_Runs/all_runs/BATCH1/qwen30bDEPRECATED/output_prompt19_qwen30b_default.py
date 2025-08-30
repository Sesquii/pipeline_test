#!/usr/bin/env python3
"""
Glitchy ASCII Artist

Converts an image to glitchy ASCII art with randomized corruption.

Usage:
    python glitchy_ascii.py --input <image_path> [--width <int>] [--output <file_path>]
"""

import argparse
import random
from PIL import Image
import sys


def main():
    parser = argparse.ArgumentParser(description="Convert an image to glitchy ASCII art.")
    parser.add_argument('--input', required=True, help='Path to the input image file')
    parser.add_argument('--width', type=int, default=80, help='Maximum width in characters (default: 80)')
    parser.add_argument('--output', default='output.txt', help='Output file path (default: output.txt)')

    args = parser.parse_args()

    try:
        # Load and process image
        with Image.open(args.input) as img:
            # Convert to grayscale
            grayscale_img = img.convert('L')
            
            # Scale image while preserving aspect ratio
            width, height = grayscale_img.size
            aspect_ratio = height / width
            new_width = args.width
            new_height = int(new_width * aspect_ratio * 0.5)  # Adjust for character aspect ratio
            
            resized_img = grayscale_img.resize((new_width, new_height))
            
            # ASCII characters from darkest to lightest
            ascii_chars = '@%#*+=-:. '
            
            # Convert pixels to ASCII
            ascii_art = ''
            for y in range(new_height):
                for x in range(new_width):
                    pixel_value = resized_img.getpixel((x, y))
                    # Map pixel intensity (0-255) to index in ascii_chars
                    char_index = int(pixel_value / 255 * (len(ascii_chars) - 1))
                    ascii_art += ascii_chars[char_index]
                ascii_art += '\n'
            
            # Apply glitch effect: randomly corrupt 10% of characters
            random.seed(42)
            char_list = list(ascii_art)
            num_corrupt = int(len(char_list) * 0.1)
            corrupt_indices = random.sample(range(len(char_list)), num_corrupt)
            
            for i in corrupt_indices:
                if char_list[i] == '\n':
                    continue  # Don't corrupt newlines
                # Replace with either another ASCII character or space
                if random.random() < 0.5:
                    char_list[i] = random.choice(ascii_chars)
                else:
                    char_list[i] = ' '
            
            glitched_ascii_art = ''.join(char_list)
            
            # Print to stdout
            print(glitched_ascii_art)
            
            # Write to output file
            with open(args.output, 'w') as f:
                f.write(glitched_ascii_art)
                
    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error processing image: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
