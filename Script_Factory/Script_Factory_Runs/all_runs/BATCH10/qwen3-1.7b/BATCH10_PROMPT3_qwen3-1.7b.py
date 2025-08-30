```python
import sys

def create_hologram(input_str):
    hologram = []
    for i in range(len(input_str)):
        line = " " * (len(input_str) - i - 1)
        if i < len(input_str):
            line += input_str[i]
        colored_line = f"\033[97m{line}\033[0m"
        hologram.append(colored_line)
    return "\n".join(hologram)

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    print(create_hologram(input_str))