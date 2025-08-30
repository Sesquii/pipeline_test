import random

def simulate_quantum_coin_flip():
    """
    Simulates a quantum coin flip where the result is both heads and tails until observed.
    
    Returns:
        str: 'Heads' or 'Tails' based on the simulated quantum state.
    """
    # Quantum superposition: Both states are equally likely
    outcomes = ['Heads', 'Tails']
    return random.choice(outcomes)

if __name__ == "__main__":
    result = simulate_quantum_coin_flip()
    print(f"The coin flip is observed to be {result}.")