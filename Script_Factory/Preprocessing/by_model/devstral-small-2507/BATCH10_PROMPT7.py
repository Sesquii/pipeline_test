# BATCH10_PROMPT7_Devstral.py

import random
import time

class QuantumCoin:
    def __init__(self):
        self.state = "superposition"  # Initial state is in superposition
        self.result = None

    def observe(self):
        """Simulate the observation of the quantum coin, collapsing it to a definite state."""
        if self.state == "superposition":
            self.result = random.choice(["heads", "tails"])
            self.state = "observed"
        return self.result

    def __str__(self):
        if self.state == "superposition":
            return "Quantum coin is in superposition (both heads and tails)"
        else:
            return f"Quantum coin observed: {self.result}"

def main():
    print("Simulating a quantum coin flip...")
    time.sleep(1)  # Pause to simulate the quantum nature

    coin = QuantumCoin()
    print(coin)

    print("\nObserving the coin and collapsing its state...")
    time.sleep(1)
    result = coin.observe()
    print(f"Result: {result}")

if __name__ == "__main__":
    main()