```python
import os
import sys
import random

def main():
    if len(sys.argv) < 2:
        print("Usage: python echo_finder.py <directory>")
        sys.exit(1)
    
    dir_path = sys.argv[1]
    if not os.path.isdir(dir_path):
        print(f"Directory {dir_path} does not exist.")
        sys.exit(1)
    
    # List all files in the directory, excluding directories
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    
    # Print each file repeated multiple times (2-5 times)
    for filename in files:
        count = random.randint(2, 5)
        for _ in range(count):
            print(filename)

if __name__ == "__main__":
    main()