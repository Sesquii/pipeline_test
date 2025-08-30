# BATCH2_PROMPT2_{model_name}.py

import re

def reverse_markdown_converter(html_string):
    """
    Convert HTML or rich-text string to simplified markdown format using regular expressions.

    Args:
        html_string (str): The input HTML or rich-text string

    Returns:
        str: The converted markdown string
    """

    # Remove script and style tags with content
    html_string = re.sub(r'<(script|style).*?>.*?</\1>', '', html_string, flags=re.DOTALL | re.IGNORECASE)

    # Convert <b> and <strong> to **
    html_string = re.sub(r'<(/?)(b|strong)>', r'\2', html_string)
    html_string = re.sub(r'(?<!\*)(\*\*)(.*?)\2(?!\*)', r'**\3**', html_string)

    # Convert <i> and <em> to *
    html_string = re.sub(r'<(/?)(i|em)>', r'\2', html_string)
    html_string = re.sub(r'(?<!\*)(\*)(.*?)\1(?!\*)', r'*\2*', html_string)

    # Convert <u> and <ins> to _
    html_string = re.sub(r'<(/?)(u|ins)>', r'\2', html_string)
    html_string = re.sub(r'(?<!_)(_)(.*?)\1(?!_)', r'_\2_', html_string)

    # Convert <h1> to #, <h2> to ##, etc.
    for i in range(1, 7):
        pattern = fr'<h{i}>(.*?)<\/h{i}>'
        replacement = fr'#' * i + r' \1\n'
        html_string = re.sub(pattern, replacement, html_string, flags=re.IGNORECASE)

    # Convert <p> to paragraph breaks
    html_string = re.sub(r'<p>', '\n\n', html_string)
    html_string = re.sub(r'</p>', '\n\n', html_string)

    # Convert <br> to newlines
    html_string = re.sub(r'<br\s*/?>', '\n', html_string, flags=re.IGNORECASE)

    # Convert <a href="...">...</a> to [text](url)
    html_string = re.sub(r'<a\s+href=["\'](.*?)["\']>(.*?)<\/a>', r'[\2](\1)', html_string, flags=re.IGNORECASE)

    # Convert <blockquote> to > blockquotes
    html_string = re.sub(r'<blockquote>(.*?)<\/blockquote>', r'> \1', html_string, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove remaining HTML tags
    html_string = re.sub(r'<!--.*?-->', '', html_string, flags=re.DOTALL)  # Remove comments
    html_string = re.sub(r'<[^>]+>', '', html_string)  # Remove all other tags

    return html_string.strip()

if __name__ == "__main__":
    # Example usage
    test_html = """
    <h1>Main Title</h1>
    <p>This is a <b>bold</b> and <i>italic</i> paragraph.</p>
    <p>Here's a <a href="https://example.com">link</a></p>
    <blockquote>
        This is a blockquote
    </blockquote>
    <p>Line 1<br>Line 2</p>
    """

    markdown_output = reverse_markdown_converter(test_html)
    print("Converted Markdown:")
    print(markdown_output)

# ===== GENERATED TESTS =====
# BATCH2_PROMPT2_{model_name}.py

import re

def reverse_markdown_converter(html_string):
    """
    Convert HTML or rich-text string to simplified markdown format using regular expressions.

    Args:
        html_string (str): The input HTML or rich-text string

    Returns:
        str: The converted markdown string
    """

    # Remove script and style tags with content
    html_string = re.sub(r'<(script|style).*?>.*?</\1>', '', html_string, flags=re.DOTALL | re.IGNORECASE)

    # Convert <b> and <strong> to **
    html_string = re.sub(r'<(/?)(b|strong)>', r'\2', html_string)
    html_string = re.sub(r'(?<!\*)(\*\*)(.*?)\2(?!\*)', r'**\3**', html_string)

    # Convert <i> and <em> to *
    html_string = re.sub(r'<(/?)(i|em)>', r'\2', html_string)
    html_string = re.sub(r'(?<!\*)(\*)(.*?)\1(?!\*)', r'*\2*', html_string)

    # Convert <u> and <ins> to _
    html_string = re.sub(r'<(/?)(u|ins)>', r'\2', html_string)
    html_string = re.sub(r'(?<!_)(_)(.*?)\1(?!_)', r'_\2_', html_string)

    # Convert <h1> to #, <h2> to ##, etc.
    for i in range(1, 7):
        pattern = fr'<h{i}>(.*?)<\/h{i}>'
        replacement = fr'#' * i + r' \1\n'
        html_string = re.sub(pattern, replacement, html_string, flags=re.IGNORECASE)

    # Convert <p> to paragraph breaks
    html_string = re.sub(r'<p>', '\n\n', html_string)
    html_string = re.sub(r'</p>', '\n\n', html_string)

    # Convert <br> to newlines
    html_string = re.sub(r'<br\s*/?>', '\n', html_string, flags=re.IGNORECASE)

    # Convert <a href="...">...</a> to [text](url)
    html_string = re.sub(r'<a\s+href=["\'](.*?)["\']>(.*?)<\/a>', r'[\2](\1)', html_string, flags=re.IGNORECASE)

    # Convert <blockquote> to > blockquotes
    html_string = re.sub(r'<blockquote>(.*?)<\/blockquote>', r'> \1', html_string, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove remaining HTML tags
    html_string = re.sub(r'<!--.*?-->', '', html_string, flags=re.DOTALL)  # Remove comments
    html_string = re.sub(r'<[^>]+>', '', html_string)  # Remove all other tags

    return html_string.strip()

if __name__ == "__main__":
    # Example usage
    test_html = """
    <h1>Main Title</h1>
    <p>This is a <b>bold</b> and <i>italic</i> paragraph.</p>
    <p>Here's a <a href="https://example.com">link</a></p>
    <blockquote>
        This is a blockquote
    </blockquote>
    <p>Line 1<br>Line 2</p>
    """

    markdown_output = reverse_markdown_converter(test_html)
    print("Converted Markdown:")
    print(markdown_output)

# Test suite for reverse_markdown_converter function

import pytest

@pytest.fixture
def sample_html():
    return """
    <h1>Main Title</h1>
    <p>This is a <b>bold</b> and <i>italic</i> paragraph.</p>
    <p>Here's a <a href="https://example.com">link</a></p>
    <blockquote>
        This is a blockquote
    </blockquote>
    <p>Line 1<br>Line 2</p>
    """

@pytest.fixture
def expected_markdown():
    return """
# Main Title

**bold** and *italic* paragraph.

[link](https://example.com)

> This is a blockquote

Line 1  
Line 2
"""

def test_reverse_markdown_converter(sample_html: str, expected_markdown: str) -> None:
    """Test the reverse_markdown_converter function with a sample HTML string."""
    assert reverse_markdown_converter(sample_html) == expected_markdown.strip()

def test_reverse_markdown_converter_empty_string() -> None:
    """Test the reverse_markdown_converter function with an empty string."""
    assert reverse_markdown_converter("") == ""

def test_reverse_markdown_converter_no_tags() -> None:
    """Test the reverse_markdown_converter function with a string that has no HTML tags."""
    assert reverse_markdown_converter("This is plain text.") == "This is plain text."

def test_reverse_markdown_converter_script_and_style_tags() -> None:
    """Test the reverse_markdown_converter function with script and style tags."""
    html = """
    <script>alert('Hello');</script>
    <style>body { color: red; }</style>
    This should not be converted.
    """
    assert reverse_markdown_converter(html) == "This should not be converted."

def test_reverse_markdown_converter_nested_tags() -> None:
    """Test the reverse_markdown_converter function with nested tags."""
    html = """
    <p>This is a <b><i>nested</i></b> tag.</p>
    """
    assert reverse_markdown_converter(html) == "**_nested_**"

def test_reverse_markdown_converter_unsupported_tags() -> None:
    """Test the reverse_markdown_converter function with unsupported tags."""
    html = """
    <div>This should not be converted.</div>
    <span>This should not be converted either.</span>
    """
    assert reverse_markdown_converter(html) == "This should not be converted.\nThis should not be converted either."

def test_reverse_markdown_converter_comments() -> None:
    """Test the reverse_markdown_converter function with HTML comments."""
    html = """
    <!-- This is a comment -->
    <p>This should be converted.</p>
    """
    assert reverse_markdown_converter(html) == "This should be converted."
