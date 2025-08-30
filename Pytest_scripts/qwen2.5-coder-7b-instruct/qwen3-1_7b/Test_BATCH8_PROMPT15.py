```python
import sys
from collections import defaultdict

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    adjusted_counts = {}
    for word, count in word_counts.items():
        e_count = word.count('e')
        if e_count > 3:
            adjusted_counts[word] = count * 3
        else:
            adjusted_counts[word] = count
    print(adjusted_counts)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import pytest
from collections import defaultdict

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    adjusted_counts = {}
    for word, count in word_counts.items():
        e_count = word.count('e')
        if e_count > 3:
            adjusted_counts[word] = count * 3
        else:
            adjusted_counts[word] = count
    print(adjusted_counts)

if __name__ == "__main__":
    main()

# Test suite starts here

def test_main_no_args(capsys):
    """Test that the script prints usage message when no arguments are provided."""
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "Usage: python script.py <filename>" in captured.err

def test_main_invalid_file(capsys):
    """Test that the script prints an error message when an invalid file is provided."""
    with pytest.raises(SystemExit) as excinfo:
        main(['script.py', 'nonexistentfile.txt'])
    assert excinfo.value.code == 1
    captured = capsys.readouterr()
    assert "Error: File not found" in captured.err

def test_main_empty_file(capsys):
    """Test that the script prints an empty dictionary when an empty file is provided."""
    with open('emptyfile.txt', 'w') as f:
        pass
    main(['script.py', 'emptyfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == '{}\n'

def test_main_single_word_file(capsys):
    """Test that the script correctly counts a single word in a file."""
    with open('singlewordfile.txt', 'w') as f:
        f.write("hello")
    main(['script.py', 'singlewordfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1}\n"

def test_main_multiple_words_file(capsys):
    """Test that the script correctly counts multiple words in a file."""
    with open('multiplewordsfile.txt', 'w') as f:
        f.write("hello world hello")
    main(['script.py', 'multiplewordsfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 2, 'world': 1}\n"

def test_main_word_with_multiple_es(capsys):
    """Test that the script correctly adjusts counts for words with multiple 'e's."""
    with open('multipleesfile.txt', 'w') as f:
        f.write("bee bee bee")
    main(['script.py', 'multipleesfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'bee': 9}\n"

def test_main_word_with_single_e(capsys):
    """Test that the script correctly adjusts counts for words with a single 'e'."""
    with open('singleefile.txt', 'w') as f:
        f.write("see sea")
    main(['script.py', 'singleefile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'see': 1, 'sea': 1}\n"

def test_main_word_with_no_e(capsys):
    """Test that the script correctly adjusts counts for words with no 'e's."""
    with open('noefile.txt', 'w') as f:
        f.write("sky fly")
    main(['script.py', 'noefile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'sky': 1, 'fly': 1}\n"

def test_main_word_with_special_chars(capsys):
    """Test that the script correctly counts words with special characters."""
    with open('specialcharsfile.txt', 'w') as f:
        f.write("hello! world?")
    main(['script.py', 'specialcharsfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_numbers(capsys):
    """Test that the script correctly counts words with numbers."""
    with open('numbersfile.txt', 'w') as f:
        f.write("123 456 789")
    main(['script.py', 'numbersfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'123': 1, '456': 1, '789': 1}\n"

def test_main_word_with_uppercase(capsys):
    """Test that the script correctly counts words with uppercase letters."""
    with open('uppercasefile.txt', 'w') as f:
        f.write("Hello World")
    main(['script.py', 'uppercasefile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_lowercase(capsys):
    """Test that the script correctly counts words with lowercase letters."""
    with open('lowercasefile.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', 'lowercasefile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_mixed_case(capsys):
    """Test that the script correctly counts words with mixed case letters."""
    with open('mixedcasefile.txt', 'w') as f:
        f.write("Hello World hello")
    main(['script.py', 'mixedcasefile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 2, 'world': 1}\n"

def test_main_word_with_punctuation(capsys):
    """Test that the script correctly counts words with punctuation."""
    with open('punctuationfile.txt', 'w') as f:
        f.write("hello! world?")
    main(['script.py', 'punctuationfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_space(capsys):
    """Test that the script correctly counts words with spaces."""
    with open('spacefile.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', 'spacefile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_tab(capsys):
    """Test that the script correctly counts words with tabs."""
    with open('tabfile.txt', 'w') as f:
        f.write("hello\tworld")
    main(['script.py', 'tabfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_newline(capsys):
    """Test that the script correctly counts words with newlines."""
    with open('newlinefile.txt', 'w') as f:
        f.write("hello\nworld")
    main(['script.py', 'newlinefile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_carriage_return(capsys):
    """Test that the script correctly counts words with carriage returns."""
    with open('carriagereturnfile.txt', 'w') as f:
        f.write("hello\rworld")
    main(['script.py', 'carriagereturnfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_form_feed(capsys):
    """Test that the script correctly counts words with form feeds."""
    with open('formfeedfile.txt', 'w') as f:
        f.write("hello\fworld")
    main(['script.py', 'formfeedfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_vertical_tab(capsys):
    """Test that the script correctly counts words with vertical tabs."""
    with open('verticaltabfile.txt', 'w') as f:
        f.write("hello\vworld")
    main(['script.py', 'verticaltabfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_backspace(capsys):
    """Test that the script correctly counts words with backspaces."""
    with open('backspacefile.txt', 'w') as f:
        f.write("hello\bworld")
    main(['script.py', 'backspacefile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_escape(capsys):
    """Test that the script correctly counts words with escape characters."""
    with open('escapefile.txt', 'w') as f:
        f.write("hello\eworld")
    main(['script.py', 'escapefile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_null(capsys):
    """Test that the script correctly counts words with null characters."""
    with open('nullfile.txt', 'w') as f:
        f.write("hello\0world")
    main(['script.py', 'nullfile.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_space_in_filename(capsys):
    """Test that the script correctly counts words with a space in the filename."""
    with open('space in filename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', 'space in filename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_special_characters_in_filename(capsys):
    """Test that the script correctly counts words with special characters in the filename."""
    with open('special#characters$filename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', 'special#characters$filename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_numbers_in_filename(capsys):
    """Test that the script correctly counts words with numbers in the filename."""
    with open('numbers123filename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', 'numbers123filename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_uppercase_in_filename(capsys):
    """Test that the script correctly counts words with uppercase letters in the filename."""
    with open('UPPERCASEFILENAME.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', 'UPPERCASEFILENAME.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_lowercase_in_filename(capsys):
    """Test that the script correctly counts words with lowercase letters in the filename."""
    with open('lowercasefilename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', 'lowercasefilename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_mixed_case_in_filename(capsys):
    """Test that the script correctly counts words with mixed case letters in the filename."""
    with open('MixedCaseFilename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', 'MixedCaseFilename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_punctuation_in_filename(capsys):
    """Test that the script correctly counts words with punctuation in the filename."""
    with open('punctuationfilename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', 'punctuationfilename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_space_in_path(capsys):
    """Test that the script correctly counts words with a space in the path."""
    with open('/path/with/space/filename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with/space/filename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_special_characters_in_path(capsys):
    """Test that the script correctly counts words with special characters in the path."""
    with open('/path/with/special#characters$filename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with/special#characters$filename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_numbers_in_path(capsys):
    """Test that the script correctly counts words with numbers in the path."""
    with open('/path/with/numbers123filename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with/numbers123filename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_uppercase_in_path(capsys):
    """Test that the script correctly counts words with uppercase letters in the path."""
    with open('/path/with/UPPERCASEFILENAME.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with/UPPERCASEFILENAME.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_lowercase_in_path(capsys):
    """Test that the script correctly counts words with lowercase letters in the path."""
    with open('/path/with/lowercasefilename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with/lowercasefilename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_mixed_case_in_path(capsys):
    """Test that the script correctly counts words with mixed case letters in the path."""
    with open('/path/with/MixedCaseFilename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with/MixedCaseFilename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_punctuation_in_path(capsys):
    """Test that the script correctly counts words with punctuation in the path."""
    with open('/path/with/punctuationfilename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with/punctuationfilename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_space_in_filename_and_path(capsys):
    """Test that the script correctly counts words with a space in the filename and path."""
    with open('/path/with/space/filename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with/space/filename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_special_characters_in_filename_and_path(capsys):
    """Test that the script correctly counts words with special characters in the filename and path."""
    with open('/path/with/special#characters$filename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with/special#characters$filename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_numbers_in_filename_and_path(capsys):
    """Test that the script correctly counts words with numbers in the filename and path."""
    with open('/path/with/numbers123filename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with/numbers123filename.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_uppercase_in_filename_and_path(capsys):
    """Test that the script correctly counts words with uppercase letters in the filename and path."""
    with open('/path/with/UPPERCASEFILENAME.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with/UPPERCASEFILENAME.txt'])
    captured = capsys.readouterr()
    assert captured.out == "{'hello': 1, 'world': 1}\n"

def test_main_word_with_lowercase_in_filename_and_path(capsys):
    """Test that the script correctly counts words with lowercase letters in the filename and path."""
    with open('/path/with/lowercasefilename.txt', 'w') as f:
        f.write("hello world")
    main(['script.py', '/path/with