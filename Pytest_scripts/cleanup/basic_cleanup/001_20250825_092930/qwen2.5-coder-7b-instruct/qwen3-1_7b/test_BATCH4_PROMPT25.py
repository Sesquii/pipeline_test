import random
from sys import stdin

unrelated_comments = [
    "This is an unrelated comment.",
    "A random comment here.",
    "Just a random note."
]

absurd_comments = [
    "This line is so simple it's almost useless; it's just a placeholder for a real function.",
    "The code here is so trivial that it's barely worth writing.",
    "This is an example of an absurdly detailed comment, even though the code is very short."
]

def generate_comment():
    return random.choice(unrelated_comments) if random.random() < 0.5 else random.choice(absurd_comments)

if __name__ == "__main__":
    filename = "BATCH4_PROMPT25_{{model_name}}.py"
    with open(filename, 'w') as f:
        f.write("import random\n")
        f.write("\n")
        f.write("unrelated_comments = [\n    \"This is an unrelated comment.\",\n    \"A random comment here.\",\n    \"Just a random note.\" \n]\n")
        f.write("\n")
        f.write("absurd_comments = [\n    \"This line is so simple it's almost useless; it's just a placeholder for a real function.\",\n    \"The code here is so trivial that it's barely worth writing.\",\n    \"This is an example of an absurdly detailed comment, even though the code is very short.\" \n]\n")
        f.write("\n")
        f.write("def generate_comment():\n    return random.choice(unrelated_comments) if random.random() < 0.5 else random.choice(absurd_comments)\n")
        f.write("\n")
        f.write("if __name__ == \"__main__\":\n    import sys\n    input_code = sys.stdin.read()\n    lines = input_code.splitlines()\n    modified_lines = []\n    for line in lines:\n        if random.random() < 0.5:\n            comment = generate_comment()\n            modified_line = f\"{line} #{comment}\"\n        else:\n            modified_line = line\n        modified_lines.append(modified_line)\n    print(\"\\n\".join(modified_lines))\n")

# ===== GENERATED TESTS =====
import pytest
from typing import List

# Original code
unrelated_comments = [
    "This is an unrelated comment.",
    "A random comment here.",
    "Just a random note."
]

absurd_comments = [
    "This line is so simple it's almost useless; it's just a placeholder for a real function.",
    "The code here is so trivial that it's barely worth writing.",
    "This is an example of an absurdly detailed comment, even though the code is very short."
]

def generate_comment():
    return random.choice(unrelated_comments) if random.random() < 0.5 else random.choice(absurd_comments)

# Test suite
@pytest.fixture
def sample_code() -> str:
    """Provide a sample Python code for testing."""
    return "print('Hello, World!')\ndef add(a, b): return a + b"

@pytest.fixture
def expected_output_unrelated(sample_code: str) -> List[str]:
    """Expected output with unrelated comments."""
    lines = sample_code.splitlines()
    modified_lines = []
    for line in lines:
        if random.random() < 0.5:
            comment = generate_comment()
            modified_line = f"{line} #{comment}"
        else:
            modified_line = line
        modified_lines.append(modified_line)
    return modified_lines

@pytest.fixture
def expected_output_absurd(sample_code: str) -> List[str]:
    """Expected output with absurd comments."""
    lines = sample_code.splitlines()
    modified_lines = []
    for line in lines:
        if random.random() < 0.5:
            comment = generate_comment()
            modified_line = f"{line} #{comment}"
        else:
            modified_line = line
        modified_lines.append(modified_line)
    return modified_lines

def test_generate_comment(sample_code: str, expected_output_unrelated: List[str], expected_output_absurd: List[str]):
    """Test the generate_comment function."""
    for _ in range(10):
        comment = generate_comment()
        assert comment in unrelated_comments or comment in absurd_comments
        if comment in unrelated_comments:
            modified_lines = expected_output_unrelated
        else:
            modified_lines = expected_output_absurd
        assert comment in modified_lines

def test_main(sample_code: str, expected_output_unrelated: List[str], expected_output_absurd: List[str]):
    """Test the main function."""
    with pytest.raises(SystemExit) as exc_info:
        import sys
        sys.stdin = io.StringIO(sample_code)
        exec(open("BATCH4_PROMPT25_{{model_name}}.py").read())
    assert exc_info.value.code == 0

    # Check if output contains comments
    output = sys.stdout.getvalue()
    for line in output.splitlines():
        if '#' in line:
            comment = line.split('#')[1].strip()
            assert comment in unrelated_comments or comment in absurd_comments
