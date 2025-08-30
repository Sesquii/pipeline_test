```python
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH2_PROMPT23_{{model_name}}.py <directory>")
        return
    
    dir_path = sys.argv[1]
    
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    
    for file_name in files:
        for _ in range(3):
            print(file_name)

if __name__ == "__main__":
    main()