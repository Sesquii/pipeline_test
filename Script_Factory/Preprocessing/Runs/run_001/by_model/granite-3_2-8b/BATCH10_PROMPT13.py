import os
from collections import Counter
import stat

def analyze_extensions(directory):
    extensions = []

    for path, _, files in os.walk(directory):
        for file in files:
            filename, ext = os.path.splitext(file)
            if ext and not ext[0] == '.':  # Ignore hidden files
                extensions.append(ext[1:])  # Remove the dot from the extension

    return Counter(extensions)

def generate_tribute(counter):
    lines = []

    top_three = counter.most_common(3)

    if len(top_three) == 1:
        lines.append("In a realm of data, one format doth reign.")
        lines.append(f"With {top_three[0][0]} files, it stands alone in its domain.")
    elif len(top_three) == 2:
        lines.append("Two formats vie for glory, side by side they stand.")
        lines.append(f"First with {top_three[0][0]} files, a formidable band.")
        lines.append(f"Close behind, {top_three[1][0]} holds its ground, no demand.")
    else:  # len(top_three) == 3
        lines.append("In this digital landscape, three formats vie.")
        lines.append(f"Leading the charge, {top_three[0][0]}, with files so spry.")
        lines.append(f"Next in line, {top_three[1][0]} bows with a gentle sigh.")
        lines.append(f"Close behind, {top_three[2][0]} brings up the rear, none can deny.")

    return '\n'.join(lines)

def main():
    if len(os.sys.argv) < 2:
        print("Usage: python BATCH10_PROMPT13_{model_name}.py [directory]")
        exit(1)
    
    directory = os.path.abspath(os.sys.argv[1])

    if not os.path.isdir(directory):
        print(f"The provided path '{directory}' does not exist or is not a directory.")
        exit(1)

    extension_counter = analyze_extensions(directory)
    tribute = generate_tribute(extension_counter)
    
    print("Tribute to the Most Used File Extensions:")
    print(tribute)

if __name__ == "__main__":
    main()