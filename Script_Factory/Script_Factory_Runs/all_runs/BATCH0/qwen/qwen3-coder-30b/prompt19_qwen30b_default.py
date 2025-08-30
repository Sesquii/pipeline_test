#!/usr/bin/env python3
"""
Glitchy ASCII Artist

Converts an image to glitchy ASCII art with randomized corruption.
"""

import argparse
import sys
from PIL import Image
import random


def main():
    parser = argparse.ArgumentParser(
        description="Convert an image to glitchy ASCII art.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage example:
  python glitchy_ascii.py --input image.jpg --width 80
  python glitchy_ascii.py --input image.png --output result.txt
        """
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input image file."
    )
    parser.add_argument(
        "--width",
        type=int,
        default=None,
        help="Maximum width in characters (default: no scaling)."
    )
    parser.add_argument(
        "--output",
        default="output.txt",
        help="Output file path (default: output.txt)."
    )

    args = parser.parse_args()

    try:
        # Load image
        with Image.open(args.input) as img:
            # Convert to grayscale
            gray_img = img.convert("L")

            # Scale if width is specified
            if args.width:
                aspect_ratio = gray_img.height / gray_img.width
                new_width = args.width
                new_height = int(new_width * aspect_ratio)
                gray_img = gray_img.resize((new_width, new_height), Image.LANCZOS)

            # ASCII characters ordered from darkest to lightest
            ascii_chars = "@%#*+=-:. "

            # Convert image to ASCII string
            ascii_string = ""
            for y in range(gray_img.height):
                for x in range(gray_img.width):
                    pixel = gray_img.getpixel((x, y))
                    # Map pixel intensity (0-255) to index in ascii_chars (0-9)
                    char_index = int(pixel / 255 * (len(ascii_chars) - 1))
                    ascii_string += ascii_chars[char_index]

            # Apply glitch effect: corrupt 10% of characters
            random.seed(42)
            glitch_count = int(len(ascii_string) * 0.1)
            glitch_positions = random.sample(range(len(ascii_string)), glitch_count)

            glitched_string = list(ascii_string)
            for pos in glitch_positions:
                # Replace with either another ASCII character or space
                if random.random() < 0.5:
                    # Replace with random character from set
                    new_char = random.choice(ascii_chars)
                    glitched_string[pos] = new_char
                else:
                    # Replace with space
                    glitched_string[pos] = " "

            final_ascii = "".join(glitched_string)

            # Print to stdout
            print(final_ascii)

            # Write to file
            with open(args.output, "w") as f:
                f.write(final_ascii)

    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error processing image: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
