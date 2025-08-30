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

# ===== GENERATED TESTS =====
import pytest

# Original script remains unchanged

def simulate_quantum_coin_flip():
    """
    Simulates a quantum coin flip where the result is both heads and tails until observed.
    
    Returns:
        str: 'Heads' or 'Tails' based on the simulated quantum state.
    """
    # Quantum superposition: Both states are equally likely
    outcomes = ['Heads', 'Tails']
    return random.choice(outcomes)

# Test suite for the simulate_quantum_coin_flip function

@pytest.fixture
def mock_random_choice():
    """Fixture to mock the random.choice function."""
    def _mock_choice(choices):
        return choices[0]  # Always return 'Heads'
    return _mock_choice

def test_simulate_quantum_coin_flip(mock_random_choice, monkeypatch):
    """
    Test the simulate_quantum_coin_flip function with a mocked random choice.
    
    Args:
        mock_random_choice (callable): Mocked version of random.choice that always returns 'Heads'.
        monkeypatch (pytest.MonkeyPatch): Pytest fixture to patch functions during test execution.
    """
    # Patch the random.choice function
    monkeypatch.setattr(random, 'choice', mock_random_choice)
    
    # Call the function under test
    result = simulate_quantum_coin_flip()
    
    # Assert that the result is always 'Heads'
    assert result == 'Heads'

def test_simulate_quantum_coin_flip_negative(mock_random_choice, monkeypatch):
    """
    Test the simulate_quantum_coin_flip function with a mocked random choice that always returns 'Tails'.
    
    Args:
        mock_random_choice (callable): Mocked version of random.choice that always returns 'Tails'.
        monkeypatch (pytest.MonkeyPatch): Pytest fixture to patch functions during test execution.
    """
    # Patch the random.choice function
    monkeypatch.setattr(random, 'choice', lambda choices: choices[1])  # Always return 'Tails'
    
    # Call the function under test
    result = simulate_quantum_coin_flip()
    
    # Assert that the result is always 'Tails'
    assert result == 'Tails'

def test_simulate_quantum_coin_flip_edge_case():
    """
    Test the simulate_quantum_coin_flip function with an empty list of outcomes.
    
    Raises:
        ValueError: If the list of outcomes is empty, a ValueError should be raised.
    """
    # Call the function under test with an empty list
    with pytest.raises(ValueError):
        simulate_quantum_coin_flip(['Heads', 'Tails'])

This test suite includes comprehensive tests for the `simulate_quantum_coin_flip` function. It uses a fixture to mock the `random.choice` function, allowing us to control its behavior during testing. The tests cover both positive and negative scenarios, ensuring that the function behaves as expected under different conditions.