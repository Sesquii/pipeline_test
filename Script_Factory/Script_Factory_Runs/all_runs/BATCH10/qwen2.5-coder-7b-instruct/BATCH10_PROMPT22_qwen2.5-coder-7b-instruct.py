# BATCH10_PROMPT22_{{model_name}}.py

import random

# List of possible story plots
plots = [
    "A lost hiker discovers a hidden village.",
    "A young detective uncovers a conspiracy.",
    "An inventor creates a machine that changes the world.",
    "A group of friends embark on an adventure in space.",
    "A princess must save her kingdom from invaders."
]

# Function to generate a random plot
def generate_plot():
    return random.choice(plots)

# Main function to run the Memory-Loss Storyteller
if __name__ == "__main__":
    sentence_count = 0
    
    while True:
        # Generate and print a new plot if it's the fifth sentence or the start
        if sentence_count % 5 == 0:
            current_plot = generate_plot()
            print(f"Story Plot: {current_plot}")
        
        # Increment sentence count
        sentence_count += 1
        
        # Simulate telling a sentence from the current plot
        print("Telling a sentence from the current plot.")
        
        # Prompt user to continue or exit
        if input("Do you want to continue? (yes/no): ").lower() != 'yes':
            break