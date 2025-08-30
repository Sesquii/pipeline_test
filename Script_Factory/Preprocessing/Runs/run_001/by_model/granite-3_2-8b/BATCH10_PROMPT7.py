# BATCH10_PROMPT7_Granite.py

import random

class QuantumCoin:
    def __init__(self):
        """Initialize a quantum coin state."""
        self.state = None

    def flip(self):
        """Perform a quantum coin flip.

        The coin's state is both heads and tails until observed.
        """
        # Generate a random number between 0 and 1.
        # Interpret this as the probability of the coin landing on 'Heads'.
        prob_heads = random.random()
        
        if prob_heads < 0.5:
            self.state = 'Heads'
        else:
            self.state = 'Tails'

    def observe(self):
        """Observe (get) the state of the coin.

        The observation collapses the quantum superposition into either Heads or Tails.
        """
        if self.state is None:
            raise ValueError("Coin has not been flipped yet.")
        return self.state

def main():
    # Create a new QuantumCoin instance
    coin = QuantumCoin()

    # Flip the coin (place it in superposition)
    coin.flip()

    # Print the state of the coin before observation
    print(f"The quantum state of the coin is: {coin.state}")

    # Observe (get) the state of the coin
    result = coin.observe()
    print(f"Observing the coin reveals: {result}")

if __name__ == "__main__":
    main()