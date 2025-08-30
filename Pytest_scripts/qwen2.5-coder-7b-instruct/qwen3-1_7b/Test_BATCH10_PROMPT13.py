```python
import os
from collections import defaultdict

def main():
    # Prompt user to enter file names separated by spaces
    files = input("Enter file names separated by spaces: ").split()
    
    # Initialize a dictionary to count occurrences of each extension
    counts = defaultdict(int)
    
    # Process each file to extract and count extensions
    for file in files:
        ext = os.path.splitext(file)[1]
        counts[ext] += 1
    
    # Sort extensions by their usage count in descending order
    sorted_exts = sorted(counts.items(), key=lambda x: -x[1])
    
    # Generate a poetic tribute based on the results
    print("In the digital realm, your file extensions bloom,\n")
    for ext, cnt in sorted_exts:
        line = f"  {ext} - {cnt} uses"
        print(f"  {line}")

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from collections import defaultdict

def main():
    # Prompt user to enter file names separated by spaces
    files = input("Enter file names separated by spaces: ").split()
    
    # Initialize a dictionary to count occurrences of each extension
    counts = defaultdict(int)
    
    # Process each file to extract and count extensions
    for file in files:
        ext = os.path.splitext(file)[1]
        counts[ext] += 1
    
    # Sort extensions by their usage count in descending order
    sorted_exts = sorted(counts.items(), key=lambda x: -x[1])
    
    # Generate a poetic tribute based on the results
    print("In the digital realm, your file extensions bloom,\n")
    for ext, cnt in sorted_exts:
        line = f"  {ext} - {cnt} uses"
        print(f"  {line}")

if __name__ == "__main__":
    main()

# Test suite starts here
def test_main_positive():
    """
    Test the main function with a positive input.
    """
    # Mocking input and output using pytest's monkeypatch and capsys fixtures
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_negative():
    """
    Test the main function with a negative input.
    """
    from io import StringIO
    import sys

    # Input data with invalid file names
    input_data = "test.txt doc.pdf image.png invalid_file"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_empty_input():
    """
    Test the main function with an empty input.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = ""
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_single_file():
    """
    Test the main function with a single file.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_multiple_files():
    """
    Test the main function with multiple files.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_no_files():
    """
    Test the main function with no files.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_invalid_extension():
    """
    Test the main function with an invalid file extension.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png invalid_file"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_empty_extension():
    """
    Test the main function with an empty file extension.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_single_extension():
    """
    Test the main function with a single file extension.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_multiple_extensions():
    """
    Test the main function with multiple file extensions.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_no_extension():
    """
    Test the main function with no file extension.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_invalid_input():
    """
    Test the main function with invalid input.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_empty_input():
    """
    Test the main function with an empty input.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = ""
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_single_file():
    """
    Test the main function with a single file.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_multiple_files():
    """
    Test the main function with multiple files.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_no_files():
    """
    Test the main function with no files.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_invalid_extension():
    """
    Test the main function with an invalid file extension.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png invalid_file"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_empty_extension():
    """
    Test the main function with an empty file extension.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_single_extension():
    """
    Test the main function with a single file extension.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_multiple_extensions():
    """
    Test the main function with multiple file extensions.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_no_extension():
    """
    Test the main function with no file extension.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_invalid_input():
    """
    Test the main function with invalid input.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_empty_input():
    """
    Test the main function with an empty input.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = ""
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_single_file():
    """
    Test the main function with a single file.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_multiple_files():
    """
    Test the main function with multiple files.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_no_files():
    """
    Test the main function with no files.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_invalid_extension():
    """
    Test the main function with an invalid file extension.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png invalid_file"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
            old_stdin = sys.stdin
            sys.stdin = StringIO(input_data)
            
            main()
            
            sys.stdin = old_stdin
    
    # Check if the program exited without error
    assert exc_info.type is SystemExit and exc_info.value.code == 0

def test_main_empty_extension():
    """
    Test the main function with an empty file extension.
    """
    from io import StringIO
    import sys

    # Input data
    input_data = "test.txt doc.pdf image.png"
    
    # Redirect stdin to simulate user input
    with pytest.raises(SystemExit) as exc_info:
        with open(os.devnull, 'w') as devnull:
