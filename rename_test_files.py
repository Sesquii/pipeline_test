import os
from pathlib import Path

def rename_test_files(directory):
    """
    Recursively renames test files from 'Test_*.py' to 'test_*.py' in the given directory.
    """
    renamed_count = 0
    
    # Walk through all files in the directory
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.startswith('Test_') and filename.endswith('.py'):
                old_path = Path(root) / filename
                new_filename = 'test_' + filename[5:]  # Replace 'Test_' with 'test_'
                new_path = Path(root) / new_filename
                
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")
                    renamed_count += 1
                except Exception as e:
                    print(f"Error renaming {old_path}: {e}")
    
    return renamed_count

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Rename test files to be pytest-compatible')
    parser.add_argument('directory', nargs='?', default='.', 
                       help='Directory to search for test files (default: current directory)')
    
    args = parser.parse_args()
    
    print(f"Searching for test files in: {os.path.abspath(args.directory)}")
    count = rename_test_files(args.directory)
    print(f"\nRenamed {count} test files.")
    
    if count > 0:
        print("\nNote: You may need to update any imports or references to these test files.")
    else:
        print("No files matching 'Test_*.py' pattern were found.")
