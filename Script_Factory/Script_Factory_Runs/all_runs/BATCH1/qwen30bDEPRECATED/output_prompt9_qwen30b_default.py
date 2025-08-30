#!/usr/bin/env python3
"""
Infinite Compliment Engine

This script runs an infinite loop that prints random compliments every few seconds.
With a small probability (5%), it may print an insult instead, simulating an accidental mistake.
The script can be terminated gracefully with Ctrl+C.
"""

import random
import sys
import os
import time


def initialize_random_seed():
    """Initialize the random seed from command-line argument or environment variable."""
    # Check for seed in command-line arguments
    if len(sys.argv) > 1:
        try:
            seed = int(sys.argv[1])
            random.seed(seed)
            return
        except ValueError:
            pass
    
    # Check for seed in environment variable
    seed_env = os.getenv('COMPLIMENT_ENGINE_SEED')
    if seed_env is not None:
        try:
            seed = int(seed_env)
            random.seed(seed)
            return
        except ValueError:
            pass

    # No seed provided, let random module use default behavior
    pass


def get_compliment():
    """Select and return a random compliment or insult."""
    compliments = [
        "You are awesome!",
        "Your kindness is inspiring.",
        "You have a wonderful smile.",
        "You're doing great!",
        "You're incredibly talented.",
        "Your intelligence is impressive.",
        "You make a difference in the world.",
        "You're full of energy and positivity.",
        "You're a true friend.",
        "You're wonderfully unique."
    ]
    
    insults = [
        "You are terrible at this.",
        "I've seen better effort from a sloth.",
        "Your skills are... interesting.",
        "You should stick to your day job.",
        "That was an epic fail.",
        "You're not very good at this.",
        "Maybe try again?",
        "That's a new low.",
        "You're making me question my life choices.",
        "Not even close."
    ]
    
    # 5% chance to return an insult
    if random.random() < 0.05:
        return random.choice(insults)
    
    return random.choice(compliments)


def main():
    """Main function that runs the infinite compliment engine."""
    # Initialize random seed
    initialize_random_seed()
    
    print("Starting Infinite Compliment Engine...")
    print("Press Ctrl+C to exit.")
    print("-" * 40)
    
    try:
        while True:
            compliment = get_compliment()
            print(compliment)
            time.sleep(2)  # Wait 2 seconds before next iteration
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
