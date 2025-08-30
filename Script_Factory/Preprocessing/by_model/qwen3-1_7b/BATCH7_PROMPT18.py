```python
import os
import re

def process_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace all double quotes with single quotes in the entire file
    content = re.sub(r'"', "'", content)
    
    lines = content.splitlines(True)
    processed_lines = []
    for line in lines:
        if line.startswith('def'):
            # Remove trailing comma from function parameters
            if ',' in line and line.endswith(','):
                new_line = re.sub(r',\s*$', '', line)
                processed_lines.append(new_line)
            else:
                processed_lines.append(line)
        elif line.startswith('['):
            # Remove trailing comma from list elements
            if ',' in line and line.endswith(','):
                new_line = re.sub(r',\s*$', '', line)
                processed_lines.append(new_line)
            else:
                processed_lines.append(line)
        else:
            processed_lines.append(line)
    
    processed_content = '\n'.join(processed_lines)
    with open(file_path, 'w') as f:
        f.write(processed_content)

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python BATCH7_PROMPT18_{{model_name}}.py <directory>")
        return
    
    directory = sys.argv[1]
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()