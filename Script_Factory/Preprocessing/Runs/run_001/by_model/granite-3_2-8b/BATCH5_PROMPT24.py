import sys
import random

def recursive_art(depth, char='*'):
    if depth == 0:
        return ''
    
    lines = []
    for _ in range(2**depth):
        line = recursive_art(depth-1, char)
        if random.choice([True, False]):
            line += char
        lines.append(line)
    
    return '\n'.join(lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python art_bot.py <depth>")
        sys.exit(1)

    try:
        depth = int(sys.argv[1])
    except ValueError:
        print("Depth must be an integer.")
        sys.exit(1)

    if depth < 0:
        print("Depth cannot be negative.")
        sys.exit(1)

    char_options = '*#@'
    random.shuffle(char_options)
    art = recursive_art(depth, char_options[0])
    
    print(art)

if __name__ == "__main__":
    main()