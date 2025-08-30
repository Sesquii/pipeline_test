import random

# List of predefined insults
INSULTS = [
    "You're about as useful as a screen door on a spaceship.",
    "If laughter is the best medicine, your face must be curing the world.",
    "I'd rather dance with a bear than deal with you.",
    "You're like a candle in the wind... except you're not bright and you're not blowing away.",
    "I've seen people like you on TV, but I never thought they were real.",
    "Your personality is like a light bulb - it's either off or it's screwing everything around it.",
    "You're as welcome as a skunk at a lawn party.",
    "If brains were taxed, you'd get a refund.",
    "I've seen people with your IQ get jobs pushing buttons on vending machines.",
    "You must have been born on a highway, because that's where most accidents happen."
]

def main():
    """Main function to run the conversational CLI."""
    print("Welcome to the Insult Generator! Type anything to get an insult.")
    while True:
        user_input = input("> ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        insult = random.choice(INSULTS)
        print(f"Insult: {insult}\n")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest

# List of predefined insults
INSULTS = [
    "You're about as useful as a screen door on a spaceship.",
    "If laughter is the best medicine, your face must be curing the world.",
    "I'd rather dance with a bear than deal with you.",
    "You're like a candle in the wind... except you're not bright and you're not blowing away.",
    "I've seen people like you on TV, but I never thought they were real.",
    "Your personality is like a light bulb - it's either off or it's screwing everything around it.",
    "You're as welcome as a skunk at a lawn party.",
    "If brains were taxed, you'd get a refund.",
    "I've seen people with your IQ get jobs pushing buttons on vending machines.",
    "You must have been born on a highway, because that's where most accidents happen."
]

def generate_insult():
    """Function to generate an insult randomly."""
    return random.choice(INSULTS)

def test_generate_insult():
    """Test the generate_insult function."""
    # Check if the returned value is a string
    assert isinstance(generate_insult(), str)
    
    # Check if the returned value is one of the predefined insults
    assert generate_insult() in INSULTS

# Test suite for the main function
def test_main():
    """Test the main function."""
    from io import StringIO
    import sys
    
    # Redirect stdout to capture the output
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    
    try:
        # Call the main function
        main()
        
        # Check if the welcome message is printed
        assert "Welcome to the Insult Generator!" in captured_output.getvalue()
        
        # Simulate user input and check if an insult is generated
        sys.stdin = StringIO("anything\nexit\n")
        main()
        output = captured_output.getvalue()
        assert "Insult:" in output
        assert "Goodbye!" in output
    
    finally:
        # Restore stdout
        sys.stdout = old_stdout

# Test suite for the generate_insult function with parametrization
@pytest.mark.parametrize("insult", INSULTS)
def test_generate_insult_parametrize(insult):
    """Test the generate_insult function using parametrization."""
    assert generate_insult() in INSULTS
