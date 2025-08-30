```python
import json
import sys

def digest_json(file_path):
    """Simulate digestion of a JSON file by parsing and printing its contents."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"Successfully parsed {file_path}")
            
            if isinstance(data, dict):
                print("Dictionary content:")
                for key, value in data.items():
                    print(f"  Key: {key}, Value: {value}")
            elif isinstance(data, list):
                print("List content:")
                for item in data:
                    print(f"  Item: {item}")
            else:
                print(f"File contains non-JSON data: {data}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python BATCH10_PROMPT1_{{model_name}}.py <filename>")
    else:
        filename = sys.argv[1]
        digest_json(filename)