```python
import random
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT20_{{model_name}}.py <filename>")
        return
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
    for i in range(len(lines)):
        if (i + 1) % 4 == 0:
            num_spaces = random.randint(2, 6)
            new_line = ' ' * num_spaces + lines[i]
            lines[i] = new_line
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

if __name__ == "__main__":
    main()