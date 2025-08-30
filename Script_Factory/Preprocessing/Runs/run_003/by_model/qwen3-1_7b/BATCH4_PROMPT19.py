```python
import argparse
from pathlib import Path
import random
import string
import os

def generate_random_string(length=8):
    """Generate a random string of specified length using letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def main():
    """Main function to handle the recursive file scrambler."""
    parser = argparse.ArgumentParser(description='Recursive File Scrambler')
    parser.add_argument('directory', help='Directory path to process')
    args = parser.parse_args()
    
    current_dir = Path(args.directory)
    
    if not current_dir.exists():
        print(f"Error: Directory {current_dir} does not exist.")
        return
    
    # Traverse all files and subdirectories
    for path in current_dir.glob('**/*'):
        if path.is_file():
            new_name = generate_random_string()
            os.rename(path, path.with_suffix(new_name))
            print(f"Renamed {path} to {new_name}")

if __name__ == '__main__':
    main()