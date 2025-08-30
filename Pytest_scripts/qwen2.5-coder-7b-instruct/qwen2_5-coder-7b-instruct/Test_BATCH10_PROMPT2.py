#!/usr/bin/env python3

import psutil
import random

# Function to generate a haiku based on system memory usage
def generate_memory_haiku():
    # Get the current memory usage percentage
    memory_usage = psutil.virtual_memory().percent
    
    # Define haiku templates
    templates = [
        "RAM's low, mind's foggy,\n{}% used, {}% free,\nStress grows high.",
        "Memory hums in tune,\n{}% taken by apps,\nPeaceful flow.",
        "Low memory alert,\nOnly {}% left,\nBe mindful!",
    ]
    
    # Select a random template
    selected_template = random.choice(templates)
    
    # Fill the template with actual values
    haiku = selected_template.format(memory_usage, 100 - memory_usage)
    
    return haiku

# Entry point of the program
if __name__ == "__main__":
    # Generate and print the haiku
    haiku = generate_memory_haiku()
    print(haiku)
```

Save this code in a file named `BATCH10_PROMPT2_{{model_name}}.py`. This Python script uses the `psutil` library to get the current memory usage and generates a haiku based on that usage. The program includes comments, is self-contained, and follows the specified requirements.

# ===== GENERATED TESTS =====
```python
#!/usr/bin/env python3

import psutil
import random
from typing import List

# Function to generate a haiku based on system memory usage
def generate_memory_haiku() -> str:
    # Get the current memory usage percentage
    memory_usage = psutil.virtual_memory().percent
    
    # Define haiku templates
    templates: List[str] = [
        "RAM's low, mind's foggy,\n{}% used, {}% free,\nStress grows high.",
        "Memory hums in tune,\n{}% taken by apps,\nPeaceful flow.",
        "Low memory alert,\nOnly {}% left,\nBe mindful!",
    ]
    
    # Select a random template
    selected_template = random.choice(templates)
    
    # Fill the template with actual values
    haiku = selected_template.format(memory_usage, 100 - memory_usage)
    
    return haiku

# Entry point of the program
if __name__ == "__main__":
    # Generate and print the haiku
    haiku = generate_memory_haiku()
    print(haiku)

# Test suite for the generate_memory_haiku function
import pytest

@pytest.fixture
def mock_psutil_virtual_memory():
    def mock_memory(percent: int):
        class MockMemory:
            percent = percent
        return MockMemory
    
    return mock_memory

def test_generate_memory_haiku(mock_psutil_virtual_memory):
    """Test the generate_memory_haiku function with different memory usage scenarios."""
    
    # Test with 0% memory usage
    with pytest.patch('psutil.virtual_memory', return_value=mock_psutil_virtual_memory(0)):
        haiku = generate_memory_haiku()
        assert "0% used, 100% free" in haiku
    
    # Test with 50% memory usage
    with pytest.patch('psutil.virtual_memory', return_value=mock_psutil_virtual_memory(50)):
        haiku = generate_memory_haiku()
        assert "50% used, 50% free" in haiku
    
    # Test with 100% memory usage
    with pytest.patch('psutil.virtual_memory', return_value=mock_psutil_virtual_memory(100)):
        haiku = generate_memory_haiku()
        assert "100% used, 0% free" in haiku

def test_generate_memory_haiku_random_template(mock_psutil_virtual_memory):
    """Test the generate_memory_haiku function with different memory usage scenarios and random templates."""
    
    # Test with 25% memory usage
    with pytest.patch('psutil.virtual_memory', return_value=mock_psutil_virtual_memory(25)):
        haiku = generate_memory_haiku()
        assert "25% used, 75% free" in haiku
    
    # Test with 75% memory usage
    with pytest.patch('psutil.virtual_memory', return_value=mock_psutil_virtual_memory(75)):
        haiku = generate_memory_haiku()
        assert "75% used, 25% free" in haiku

def test_generate_memory_haiku_negative_memory(mock_psutil_virtual_memory):
    """Test the generate_memory_haiku function with negative memory usage scenarios."""
    
    # Test with -10% memory usage
    with pytest.raises(ValueError):
        with pytest.patch('psutil.virtual_memory', return_value=mock_psutil_virtual_memory(-10)):
            haiku = generate_memory_haiku()
    
    # Test with 110% memory usage
    with pytest.raises(ValueError):
        with pytest.patch('psutil.virtual_memory', return_value=mock_psutil_virtual_memory(110)):
            haiku = generate_memory_haiku()

def test_generate_memory_haiku_empty_templates(mock_psutil_virtual_memory):
    """Test the generate_memory_haiku function with an empty list of templates."""
    
    # Test with 50% memory usage and no templates
    with pytest.raises(ValueError):
        with pytest.patch('psutil.virtual_memory', return_value=mock_psutil_virtual_memory(50)):
            with pytest.patch('generate_memory_haiku.templates', []):
                haiku = generate_memory_haiku()
```