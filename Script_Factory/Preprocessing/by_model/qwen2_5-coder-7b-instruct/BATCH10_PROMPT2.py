#!/usr/bin/env python3

import psutil
import random

# Function to generate a haiku based on system memory usage
def generate_memory_haiku():
    # Get the current memory usage percentage
    memory_usage = psutil.virtual_memory().percent
    
    # Define haiku templates
    templates = [
        "RAM's low, mind's foggy,\n{}% used, {}% free,\nStress grows high.",
        "Memory hums in tune,\n{}% taken by apps,\nPeaceful flow.",
        "Low memory alert,\nOnly {}% left,\nBe mindful!",
    ]
    
    # Select a random template
    selected_template = random.choice(templates)
    
    # Fill the template with actual values
    haiku = selected_template.format(memory_usage, 100 - memory_usage)
    
    return haiku

# Entry point of the program
if __name__ == "__main__":
    # Generate and print the haiku
    haiku = generate_memory_haiku()
    print(haiku)
```

Save this code in a file named `BATCH10_PROMPT2_{{model_name}}.py`. This Python script uses the `psutil` library to get the current memory usage and generates a haiku based on that usage. The program includes comments, is self-contained, and follows the specified requirements.