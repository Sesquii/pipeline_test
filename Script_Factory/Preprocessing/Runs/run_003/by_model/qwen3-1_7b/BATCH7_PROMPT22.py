```python
import sys
import random
import string

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def process_file(input_path, output_path, model_name):
    with open(input_path, 'r') as f:
        lines = [line.rstrip('\n') for line in f]
    
    processed_lines = []
    for line in lines:
        if line.startswith('#'):
            new_line = generate_random_string()
        elif '"""' in line or "''' in line:
            new_line = generate_random_string()
        else:
            new_line = line
        processed_lines.append(new_line)
    
    with open(output_path, 'w') as f:
        for line in processed_lines:
            f.write(line + '\n')

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Code Style Saboteur')
    parser.add_argument('input_file', help='Input Python file')
    parser.add_argument('--model-name', default='my_model', help='Model name for output filename')
    
    args = parser.parse_args()
    model_name = args.model_name
    output_path = f'BATCH7_PROMPT22_{model_name}.py'
    
    process_file(args.input_file, output_path, model_name)