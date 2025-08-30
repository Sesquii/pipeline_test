```python
import os
import random
import string

def generate_random_string():
    """Generates a random 10-character string using letters and digits."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=10))

def main():
    """Main function to process the directory and rename files."""
    parser = argparse.ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', help='Directory path to process')
    args = parser.parse_args()

    if not os.path.exists(args.directory):
        print(f"Error: Directory {args.directory} does not exist.")
        return

    for root, dirs, files in os.walk(args.directory):
        for file in files:
            new_name = generate_random_string()
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)

if __name__ == "__main__":
    main()