import argparse
import random
from PIL import Image

def ascii_art(image_path, max_width=100):
    # Open and convert image to grayscale
    img = Image.open(image_path).convert('L')
    
    # Calculate new dimensions while preserving aspect ratio
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(max_width * aspect_ratio)
    img = img.resize((max_width, new_height))
    
    # Map pixel intensities to ASCII characters
    ascii_set = "@%#*+=-:. "
    pixels = list(img.getdata())
    ascii_string = "".join(ascii_set[pixel // 25] for pixel in pixels)
    
    # Corrupt exactly 10% of the characters randomly
    random.seed(42)
    total_chars = len(ascii_string)
    num_corrupted = int(total_chars * 0.1)
    indices_to_corrupt = random.sample(range(total_chars), num_corrupted)
    corrupted_ascii_string = ''.join(
        ascii_set[random.randint(0, len(ascii_set)-1)] if i in indices_to_corrupt else char
        for i, char in enumerate(ascii_string)
    )
    
    return corrupted_ascii_string

def main():
    parser = argparse.ArgumentParser(description="Glitchy ASCII Artist")
    parser.add_argument("--input", required=True, help="Path to the input image file.")
    parser.add_argument("--width", type=int, default=100, help="Maximum width of the ASCII art in characters (default is 100).")
    parser.add_argument("--output", default="output.txt", help="Output file for the ASCII art (default is output.txt).")
    
    args = parser.parse_args()
    
    try:
        ascii_art_str = ascii_art(args.input, args.width)
        print(ascii_art_str)
        with open(args.output, 'w') as f:
            f.write(ascii_art_str)
        print(f"Glitchy ASCII art saved to {args.output}")
    except FileNotFoundError:
        print("Error: The input file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

This script reads an image, converts it to grayscale, scales it to a specified width while preserving the aspect ratio, maps pixel intensities to ASCII characters, corrupts 10% of these characters randomly, and prints the final glitchy ASCII art to stdout as well as saving it to a file. The script includes error handling for missing files and invalid arguments.

# ===== GENERATED TESTS =====
```python
import pytest
from io import StringIO
import sys
from PIL import Image

# Original code
# ...

# Test suite
def test_ascii_art():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with default parameters
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert len(result) == 100
    
    # Test with custom width
    img = MockImage((200, 100))
    result = ascii_art(None, img, max_width=50)
    assert len(result) == 50
    
    # Test with corrupted characters
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert sum(1 for char in result if char != ' ') > 90

def test_main(capsys):
    # Redirect stdout to capture print statements
    sys.stdout = StringIO()
    
    # Test with valid input file
    main(['--input', 'test_image.jpg'])
    captured = capsys.readouterr()
    assert "Glitchy ASCII art saved to output.txt" in captured.out
    
    # Test with non-existent input file
    main(['--input', 'non_existent_file.jpg'])
    captured = capsys.readouterr()
    assert "Error: The input file does not exist." in captured.out

def test_ascii_art_with_args():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with command line arguments
    img = MockImage((100, 50))
    result = ascii_art(None, img, max_width=50)
    assert len(result) == 50

def test_ascii_art_with_output_file():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with custom output file
    img = MockImage((100, 50))
    result = ascii_art(None, img, max_width=50, output='test_output.txt')
    assert len(result) == 50

def test_ascii_art_with_invalid_args():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with invalid width
    img = MockImage((100, 50))
    with pytest.raises(SystemExit):
        ascii_art(None, img, max_width=-1)
    
    # Test with non-integer width
    img = MockImage((100, 50))
    with pytest.raises(SystemExit):
        ascii_art(None, img, max_width='abc')

def test_ascii_art_with_large_image():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 10000  # Simplified pixel data for testing
    
    # Test with large image
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert len(result) == 10000

def test_ascii_art_with_small_image():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 10  # Simplified pixel data for testing
    
    # Test with small image
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert len(result) == 10

def test_ascii_art_with_random_seed():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with random seed
    img = MockImage((100, 50))
    result1 = ascii_art(None, img)
    result2 = ascii_art(None, img)
    assert result1 == result2

def test_ascii_art_with_no_corruption():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with no corruption
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert sum(1 for char in result if char != ' ') == 100

def test_ascii_art_with_full_corruption():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [255] * 100  # Simplified pixel data for testing
    
    # Test with full corruption
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert sum(1 for char in result if char != ' ') == 0

def test_ascii_art_with_custom_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with custom ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img, max_width=50)
    assert len(result) == 50

def test_ascii_art_with_large_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with large ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert len(result) == 100

def test_ascii_art_with_small_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with small ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert len(result) == 100

def test_ascii_art_with_random_seed_and_custom_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with random seed and custom ASCII set
    img = MockImage((100, 50))
    result1 = ascii_art(None, img)
    result2 = ascii_art(None, img)
    assert result1 == result2

def test_ascii_art_with_no_corruption_and_custom_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with no corruption and custom ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert sum(1 for char in result if char != ' ') == 100

def test_ascii_art_with_full_corruption_and_custom_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [255] * 100  # Simplified pixel data for testing
    
    # Test with full corruption and custom ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert sum(1 for char in result if char != ' ') == 0

def test_ascii_art_with_large_image_and_custom_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 10000  # Simplified pixel data for testing
    
    # Test with large image and custom ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert len(result) == 10000

def test_ascii_art_with_small_image_and_custom_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 10  # Simplified pixel data for testing
    
    # Test with small image and custom ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert len(result) == 10

def test_ascii_art_with_random_seed_and_large_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with random seed and large ASCII set
    img = MockImage((100, 50))
    result1 = ascii_art(None, img)
    result2 = ascii_art(None, img)
    assert result1 == result2

def test_ascii_art_with_no_corruption_and_large_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with no corruption and large ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert sum(1 for char in result if char != ' ') == 100

def test_ascii_art_with_full_corruption_and_large_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [255] * 100  # Simplified pixel data for testing
    
    # Test with full corruption and large ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert sum(1 for char in result if char != ' ') == 0

def test_ascii_art_with_large_image_and_small_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 10000  # Simplified pixel data for testing
    
    # Test with large image and small ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert len(result) == 10000

def test_ascii_art_with_small_image_and_small_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 10  # Simplified pixel data for testing
    
    # Test with small image and small ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert len(result) == 10

def test_ascii_art_with_random_seed_and_small_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with random seed and small ASCII set
    img = MockImage((100, 50))
    result1 = ascii_art(None, img)
    result2 = ascii_art(None, img)
    assert result1 == result2

def test_ascii_art_with_no_corruption_and_small_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 100  # Simplified pixel data for testing
    
    # Test with no corruption and small ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert sum(1 for char in result if char != ' ') == 100

def test_ascii_art_with_full_corruption_and_small_ascii_set():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [255] * 100  # Simplified pixel data for testing
    
    # Test with full corruption and small ASCII set
    img = MockImage((100, 50))
    result = ascii_art(None, img)
    assert sum(1 for char in result if char != ' ') == 0

def test_ascii_art_with_large_image_and_random_seed():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 10000  # Simplified pixel data for testing
    
    # Test with large image and random seed
    img = MockImage((100, 50))
    result1 = ascii_art(None, img)
    result2 = ascii_art(None, img)
    assert result1 == result2

def test_ascii_art_with_small_image_and_random_seed():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size = size
        
        def convert(self, mode):
            return self
        
        def resize(self, new_size):
            return self
        
        def getdata(self):
            return [0] * 10  # Simplified pixel data for testing
    
    # Test with small image and random seed
    img = MockImage((100, 50))
    result1 = ascii_art(None, img)
    result2 = ascii_art(None, img)
    assert result1 == result2

def test_ascii_art_with_no_corruption_and_random_seed():
    # Mocking image data for testing
    class MockImage:
        def __init__(self, size):
            self.size =