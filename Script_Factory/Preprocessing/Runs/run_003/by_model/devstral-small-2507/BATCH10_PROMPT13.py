# BATCH10_PROMPT13_Devstral.py

import os
from collections import Counter
import random

def analyze_file_extensions(directory):
    """
    Analyzes file extensions in the given directory and returns a counter of extension frequencies.
    
    Args:
        directory (str): Path to the directory to scan for files.
        
    Returns:
        Counter: A counter object with file extensions as keys and their counts as values.
    """
    extension_counter = Counter()
    
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if '.' in file:
                    ext = file.split('.')[-1].lower()
                    extension_counter[ext] += 1
    except PermissionError as e:
        print(f"Permission error accessing {root}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return extension_counter

def generate_poetic_tribute(extensions):
    """
    Generates a short, poetic tribute to the most used file extensions.
    
    Args:
        extensions (Counter): Counter object with file extensions and their counts.
        
    Returns:
        str: A poetic tribute string.
    """
    if not extensions:
        return "No files found to celebrate!"
    
    # Get the most common extension
    most_common_ext = extensions.most_common(1)[0][0]
    
    # Poetic elements
    adjectives = ["venerable", "ubiquitous", "essential", "versatile", "invaluable"]
    verbs = ["powering", "driving", "fueling", "enabling", "supporting"]
    nouns = ["innovation", "creativity", "progress", "development", "excellence"]
    
    # Randomly select elements for the tribute
    adj = random.choice(adjectives)
    verb = random.choice(verbs)
    noun = random.choice(nouns)
    
    return (
        f"In the realm of digital creation, the {adj} '{most_common_ext}' extension stands tall,\n"
        f"{verb.capitalize()} the very essence of {noun}. A testament to our collective journey,\n"
        f"it echoes through every line of code and every pixel painted."
    )

def main():
    """
    Main entry point for the program. Analyzes file extensions in the current directory
    and generates a poetic tribute to the most used extension.
    """
    # Set the directory to analyze (current directory by default)
    directory_to_analyze = os.getcwd()
    
    print(f"Analyzing file extensions in: {directory_to_analyze}")
    
    # Analyze file extensions
    extensions = analyze_file_extensions(directory_to_analyze)
    
    if not extensions:
        print("No files found to analyze.")
        return
    
    print("\nFile extension analysis:")
    for ext, count in extensions.most_common():
        print(f"{ext}: {count} files")
    
    # Generate and display the poetic tribute
    tribute = generate_poetic_tribute(extensions)
    print("\n" + "="*60)
    print("A Poetic Tribute to Your Most Used File Extensions:")
    print(tribute)
    print("="*60)

if __name__ == "__main__":
    main()