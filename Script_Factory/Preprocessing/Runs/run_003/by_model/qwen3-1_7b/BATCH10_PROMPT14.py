```python
import os
import hashlib
import sys

def compute_sha256(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        return hashlib.sha256(data).hexdigest()

def main():
    if len(sys.argv) < 2:
        print("Usage: python scrambler.py <directory>")
        return
    
    dir_path = sys.argv[1]
    
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        
        if not os.path.isfile(file_path):
            continue
        
        sha256_hash = compute_sha256(file_path)
        
        parts = filename.split('.')
        base_part = parts[0] if len(parts) >= 1 else ''
        ext_part = parts[-1] if len(parts) >= 2 else ''
        new_filename = f"{sha256_hash}{base_part}.{ext_part}"
        
        os.rename(file_path, os.path.join(dir_path, new_filename))
    
    print("Renaming completed.")

if __name__ == "__main__":
    main()