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

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO
import sys
import os

# Original script code
def main():
    seed = None
    if len(sys.argv) > 1:
        seed = int(sys.argv[1])
    elif 'SEED' in os.environ:
        seed = int(os.environ['SEED'])
    
    random.seed(seed)
    
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
    
    while True:
        if random.random() <= 0.05:
            print(random.choice(insults))
        else:
            print(random.choice(compliments))
        
        time.sleep(2)

# Test suite
def test_main_with_seed():
    """Test main function with a seed to ensure reproducibility"""
    seed = 42
    sys.argv[1] = str(seed)
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    main()
    sys.stdout = old_stdout
    output = mystdout.getvalue().strip()
    assert "You're amazing!" in output or "You're terrible!" in output

def test_main_without_seed():
    """Test main function without a seed"""
    del os.environ['SEED']
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    main()
    sys.stdout = old_stdout
    output = mystdout.getvalue().strip()
    assert "You're amazing!" in output or "You're terrible!" in output

def test_main_keyboard_interrupt():
    """Test graceful handling of KeyboardInterrupt"""
    with pytest.raises(KeyboardInterrupt):
        main()

# Run the tests
if __name__ == "__main__":
    pytest.main(['-v', '-s'])
```

This test suite includes:
1. A test case to ensure that the `main` function produces output when a seed is provided.
2. Another test case to ensure that the `main` function produces output without a seed.
3. A test case to verify graceful handling of `KeyboardInterrupt`.
4. The tests are run using pytest with verbose and interactive options for better visibility during execution.