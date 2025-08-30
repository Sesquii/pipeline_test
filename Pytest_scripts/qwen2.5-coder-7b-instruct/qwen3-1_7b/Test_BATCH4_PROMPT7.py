```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Conversational CLI with confirmation")
    parser.add_argument('--confirm', action='store_true', help="Trigger chatty confirmation")
    args = parser.parse_args()

    if args.confirm:
        print("Confirming... (unhelpful message)")
        # No further actions here, as the script is designed to be simple and clean

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
```python
import argparse
from unittest.mock import patch
import pytest

# Original code
def main():
    parser = argparse.ArgumentParser(description="Conversational CLI with confirmation")
    parser.add_argument('--confirm', action='store_true', help="Trigger chatty confirmation")
    args = parser.parse_args()

    if args.confirm:
        print("Confirming... (unhelpful message)")
        # No further actions here, as the script is designed to be simple and clean

if __name__ == "__main__":
    main()

# Test cases
def test_main_without_confirm(capsys):
    """Test that main function does nothing when --confirm is not provided."""
    with patch('sys.argv', ['script.py']):
        main()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""

@patch('argparse.ArgumentParser.parse_args')
def test_main_with_confirm(mock_parse_args, capsys):
    """Test that main function prints confirmation message when --confirm is provided."""
    mock_parse_args.return_value.confirm = True
    with patch('sys.argv', ['script.py', '--confirm']):
        main()
    captured = capsys.readouterr()
    assert captured.out == "Confirming... (unhelpful message)\n"
    assert captured.err == ""

def test_main_with_invalid_arg(capsys):
    """Test that main function handles invalid arguments gracefully."""
    with patch('sys.argv', ['script.py', '--invalid']):
        main()
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err.startswith("usage: script.py [-h] [--confirm]")
```