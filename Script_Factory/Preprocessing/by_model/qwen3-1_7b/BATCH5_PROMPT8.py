```python
import sys

def poetic_data_visualizer(data):
    for s in data:
        words = s.split()
        line_count = len(words)
        if line_count == 1:
            print(f"{s}")
        else:
            print(f"{line_count} word{'s' if line_count > 1 else ''}")

if __name__ == "__main__":
    data = input("Enter list of strings separated by spaces: ").split()
    poetic_data_visualizer(data)