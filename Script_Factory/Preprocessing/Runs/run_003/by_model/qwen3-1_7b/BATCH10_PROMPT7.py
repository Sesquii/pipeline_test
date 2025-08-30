```python
import random

def simulate_quantum_coin_flip():
    while True:
        # Generate a random outcome for the coin flip
        result = random.choice(['heads', 'tails'])
        print(f"Observed: {result}")
        break  # The loop exits once an observation is made

if __name__ == "__main__":
    simulate_quantum_coin_flip()