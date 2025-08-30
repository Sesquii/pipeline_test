```python
import argparse
import os
import random
from PIL import Image
import sys

def main():
    parser = argparse.ArgumentParser(description='Glitchy ASCII Artist')
    parser.add_argument('--input', required=True)
    parser.add_argument('--width', type=int, help='Maximum width in characters')
    parser.add_argument('--output', default='output.txt')
    args = parser.parse_args()

    # Check if input file exists
    if not os.path.exists(args.input):
        raise FileNotFoundError(f"Input file {args.input} does not exist.")

    try:
        img = Image.open(args.input)
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)

    original_width, original_height = img.size

    if args.width is not None:
        new_width = args.width
        new_height = int((original_height / original_width) * new_width)
    else:
        new_width = original_width
        new_height = original_height

    # Convert to grayscale
    img_grayscale = img.convert('L')

    # Get pixels
    pixels = img_grayscale.load()

    # Determine the ASCII characters set
    chars = ['@', '%', '#', '*', '=', '+', '-', ':', '.']

    # Generate the ASCII string
    ascii_str = []
    rows = new_height
    cols = new_width

    for y in range(rows):
        row = []
        for x in range(cols):
            intensity = pixels[x][y]
            normalized = intensity / 255.0
            index = int(normalized * 9)
            char = chars[index]
            row.append(char)
        ascii_str.append(''.join(row))

    # Apply glitch: replace 10% of characters
    num_replacements = len(ascii_str) * 0.1
    replaced_indices = set(random.sample(range(len(ascii_str)), int(num_replacements)))
    for idx in replaced_indices:
        ascii_str[idx] = random.choice(chars)

    # Print and save to file
    print(''.join(ascii_str))
    with open(args.output, 'w') as f:
        f.write(''.join(ascii_str))

if __name__ == '__main__':
    main()