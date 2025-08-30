```python
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Echo-Based File Finder')
    parser.add_argument('directory', help='Directory to process')
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a directory.")
        return

    # List all files in the specified directory, excluding subdirectories
    for filename in os.listdir(args.directory):
        file_path = os.path.join(args.directory, filename)
        if os.path.isfile(file_path):
            # Repeat each filename three times
            for _ in range(3):
                print(filename)

if __name__ == "__main__":
    main()