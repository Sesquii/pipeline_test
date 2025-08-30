import random
import sys
import time
from datetime import datetime

# Module docstring:
"""
Infinite Compliment Engine
-------------------------

This script generates random compliments and insults in an infinite loop,
printing one every few seconds until manually terminated. It uses a 5% chance
of selecting an insult instead of a compliment to simulate accidental mistakes.
The selection can be seeded for reproducible results if desired via command-line
argument or environment variable.
"""

# Predefined lists of compliments and insults
COMPLIMENTS = [
    "You're doing a fantastic job!",
    "Your creativity is inspiring.",
    "Great effort today!",
    "I appreciate your hard work.",
    "You've got tremendous potential."
]

INSULTS = [
    "Well, that's one way to do it...",
    "Try again next time?",
    "Not your finest moment.",
    "Keep practicing.",
    "A bit off the mark today."
]

def get_seed():
    """Get seed value from command line argument or environment variable."""
    seed_val = None
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'seed':
        seed_val = int(sys.argv[2], 0)
    elif 'SEED' in os.environ:
        seed_val = int(os.environ['SEED'], 0)
    return seed_val

def main():
    """Main function for the Infinite Compliment Engine."""
    # Get seed from command line or environment, if provided
    seed_val = get_seed()

    # Set random seed for reproducibility
    if seed_val is not None:
        random.seed(seed_val)

    while True:
        try:
            # Select a random compliment or insult
            choice = random.choice([comp for comp in COMPLIMENTS + INSULTS])
            
            if random.random() < 0.05:
                print(INSULTS[random.randint(0, len(INSULTS) - 1)])
            else:
                print(choice)
                
            # Sleep for a few seconds before next iteration
            time.sleep(2)

        except KeyboardInterrupt:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()