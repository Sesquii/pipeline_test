import os

def process_python_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace double-quotes with single-quotes
    content = content.replace('"', "'")
    
    # Remove trailing commas from function calls and list definitions
    lines = content.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        if ',' in line:
            if line.strip().endswith(','):
                line = line.rstrip(',') + '\n'
                lines[i] = line
    
    new_content = ''.join(lines)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def traverse_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                process_python_file(file_path)

if __name__ == "__main__":
    # Specify the directory containing your Python project
    project_directory = 'path_to_your_project'
    
    traverse_directory(project_directory)
```

This script defines a `process_python_file` function that reads a Python file, replaces double-quotes with single-quotes, and removes trailing commas from function calls and list definitions. It then writes the modified content back to the file. The `traverse_directory` function recursively traverses the specified directory and applies `process_python_file` to each Python file it finds. The entry point checks if the script is being run directly and specifies the project directory to process.