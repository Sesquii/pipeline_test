```python
import random
import time
import sys
import os

"""Infinite Compliment Engine

This script runs an infinite loop, printing random compliments or insults every 2 seconds.
It has a 5% chance of selecting an insult instead of a compliment.
The seed can be set via command line argument or environment variable for reproducibility.
"""

def main():
    # Seed the random module based on command line argument or environment variable
    seed = None
    if len(sys.argv) > 1:
        seed = int(sys.argv[1])
    elif 'SEED' in os.environ:
        seed = int(os.environ['SEED'])
    
    # Initialize random number generator
    random.seed(seed)
    
    # Predefined lists for compliments and insults
    compliments = [
        "You're amazing!",
        "You're great!",
        "You're awesome!",
        "You're the best!"
    ]
    insults = [
        "You're terrible!",
        "You're so bad at everything!",
        "You're a disaster!"
    ]
    
    # Main loop
    while True:
        # Select random compliment or insult with 5% chance of insult
        if random.random() <= 0.05:
            print(random.choice(insults))
        else:
            print(random.choice(compliments))
        
        # Wait for 2 seconds before next iteration
        time.sleep(2)

# Gracefully handle KeyboardInterrupt
try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("Goodbye!")