import random
import sys

def swap_if_else_blocks(code):
    lines = code.split('\n')
    modified_lines = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('if ') and ':' in line:
            # Find the corresponding else block
            if_indent = len(line) - len(line.lstrip())
            else_found = False
            else_line = None
            end_if = False

            for j in range(i + 1, len(lines)):
                current_line = lines[j].strip()
                current_indent = len(lines[j]) - len(lines[j].lstrip())

                if current_line.startswith('else:') and current_indent == if_indent:
                    else_found = True
                    else_line = j
                    break
                elif current_indent <= if_indent:
                    break

            if else_found:
                # With 30% chance, swap the if and else blocks
                if random.random() < 0.3:
                    # Collect all lines of the if block
                    if_block = []
                    in_if_block = True
                    for k in range(i, else_line):
                        if lines[k].strip().startswith('elif') or lines[k].strip().startswith('else'):
                            in_if_block = False
                        if in_if_block:
                            if_block.append(lines[k])

                    # Collect all lines of the else block  
                    else_block = []
                    in_else_block = True
                    for k in range(else_line, len(lines)):
                        current_line = lines[k].strip()
                        current_indent = len(lines[k]) - len(lines[k].lstrip())
                        if current_indent <= if_indent:
                            in_else_block = False
                        if in_else_block:
                            else_block.append(lines[k])

                    # Swap the blocks
                    for k in range(i, else_line + 1):
                        if k == else_line:
                            modified_lines.extend(if_block)
                        elif k < else_line:
                            modified_lines.append(lines[k])
                        else:
                            modified_lines.extend(else_block[i + len(if_block):])
                    
                    i = else_line + len(else_block) - 1
                    continue

        modified_lines.append(lines[i])
        i += 1

    return '\n'.join(modified_lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python BATCH7_PROMPT23_Devstral.py <python_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            code = file.read()

        modified_code = swap_if_else_blocks(code)

        output_file = f"modified_{input_file}"
        with open(output_file, 'w') as file:
            file.write(modified_code)

        print(f"Modified code saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()