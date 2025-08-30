import sys
from collections import defaultdict

def process_file(filename):
    """Process a text file to count words and exaggerate counts over 5."""
    with open(filename, 'r') as f:
        text = f.read()
        words = text.split()
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1
    result = {}
    for word, count in counts.items():
        if count > 5:
            result[word] = 2 * count
        else:
            result[word] = count
    return result

def main():
    """Entry point of the script."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    filename = sys.argv[1]
    output = process_file(filename)
    print(output)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
import pytest

# Original script code
import sys
from collections import defaultdict

def process_file(filename):
    """Process a text file to count words and exaggerate counts over 5."""
    with open(filename, 'r') as f:
        text = f.read()
        words = text.split()
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1
    result = {}
    for word, count in counts.items():
        if count > 5:
            result[word] = 2 * count
        else:
            result[word] = count
    return result

def main():
    """Entry point of the script."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    filename = sys.argv[1]
    output = process_file(filename)
    print(output)

if __name__ == "__main__":
    main()

# Test cases
def test_process_file_positive():
    """Test the process_file function with a file containing words."""
    # Create a temporary file with some content
    with open('test.txt', 'w') as f:
        f.write("hello world hello hello")
    
    result = process_file('test.txt')
    assert result == {'hello': 6, 'world': 2}
    
    # Clean up the temporary file
    import os
    os.remove('test.txt')

def test_process_file_negative():
    """Test the process_file function with an empty file."""
    # Create a temporary empty file
    with open('test_empty.txt', 'w'):
        pass
    
    result = process_file('test_empty.txt')
    assert result == {}
    
    # Clean up the temporary file
    import os
    os.remove('test_empty.txt')

def test_process_file_nonexistent():
    """Test the process_file function with a non-existent file."""
    with pytest.raises(FileNotFoundError):
        process_file('non_existent_file.txt')

def test_main_positive(capsys):
    """Test the main function with a valid filename."""
    # Create a temporary file with some content
    with open('test_main.txt', 'w') as f:
        f.write("hello world hello hello")
    
    # Run the main function with the temporary file
    sys.argv = ['script.py', 'test_main.txt']
    main()
    
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 6, 'world': 2}\n"
    
    # Clean up the temporary file
    import os
    os.remove('test_main.txt')

def test_main_negative(capsys):
    """Test the main function with an invalid filename."""
    sys.argv = ['script.py', 'non_existent_file.txt']
    main()
    
    captured = capsys.readouterr()
    assert captured.out == "Usage: python script.py <filename>\n"

# Test fixtures
@pytest.fixture
def setup_teardown():
    """Setup and teardown for tests that create temporary files."""
    # Create a temporary file with some content
    open('temp_file.txt', 'w').write("hello world hello hello")
    
    yield
    
    # Clean up the temporary file
    import os
    os.remove('temp_file.txt')

# Parametrized test cases
@pytest.mark.parametrize("filename, expected", [
    ('test_param1.txt', {'hello': 6, 'world': 2}),
    ('test_param2.txt', {}),
])
def test_process_file_parametrized(filename, expected):
    """Test the process_file function with parametrized filenames."""
    # Create a temporary file with some content
    with open(filename, 'w') as f:
        f.write("hello world hello hello")
    
    result = process_file(filename)
    assert result == expected
    
    # Clean up the temporary file
    import os
    os.remove(filename)

# Test cases using setup_teardown fixture
def test_main_with_fixture(capsys, setup_teardown):
    """Test the main function with a valid filename using a fixture."""
    sys.argv = ['script.py', 'temp_file.txt']
    main()
    
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 6, 'world': 2}\n"
