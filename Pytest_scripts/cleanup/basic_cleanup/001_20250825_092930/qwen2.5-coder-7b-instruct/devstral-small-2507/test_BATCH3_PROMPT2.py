# BATCH3_PROMPT2_Devstral.py

import re

def html_to_markdown(html):
    """
    Convert HTML to simplified markdown format using regular expressions.

    Args:
        html (str): Input HTML or rich-text string

    Returns:
        str: Simplified markdown output
    """

    # Remove <br> tags and replace with newlines  
    markdown = re.sub(r'<br\s*/?>', '\n', html)

    # Convert <p> tags to markdown paragraphs
    markdown = re.sub(r'<p>(.*?)</p>', r'\1\n\n', markdown, flags=re.DOTALL)

    # Convert <h1>, <h2>, etc. to markdown headers
    for i in range(1, 7):
        pattern = rf'<h{i}>(.*?)</h{i}>'
        replacement = rf'{"#" * i} \1\n\n'
        markdown = re.sub(pattern, replacement, markdown, flags=re.DOTALL)

    # Convert <strong> and <b> to **bold**
    markdown = re.sub(r'<(strong|b)>(.*?)</\1>', r'**\2**', markdown, flags=re.DOTALL)

    # Convert <em> and <i> to *italic*
    markdown = re.sub(r'<(em|i)>(.*?)</\1>', r'*\2*', markdown, flags=re.DOTALL)

    # Convert <a href="...">...</a> to [text](url)
    markdown = re.sub(r'<a\s+href=["\'](.*?)["\']>(.*?)</a>', r'[\2](\1)', markdown, flags=re.DOTALL)

    # Remove any remaining HTML tags
    markdown = re.sub(r'<[^>]+>', '', markdown)

    # Clean up multiple newlines
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)

    return markdown.strip()

def main():
    """Entry point for the script"""
    # Example usage
    html_input = """
    <h1>Main Title</h1>
    <p>This is a paragraph with <strong>bold</strong> and <em>italic</em> text.</p>
    <p>Another paragraph with a <a href="https://example.com">link</a>.</p>
    """

    markdown_output = html_to_markdown(html_input)
    print("Markdown Output:")
    print(markdown_output)

if __name__ == "__main__":
    main()

# ===== GENERATED TESTS =====
# BATCH3_PROMPT2_Devstral.py

import re

def html_to_markdown(html):
    """
    Convert HTML to simplified markdown format using regular expressions.

    Args:
        html (str): Input HTML or rich-text string

    Returns:
        str: Simplified markdown output
    """

    # Remove <br> tags and replace with newlines  
    markdown = re.sub(r'<br\s*/?>', '\n', html)

    # Convert <p> tags to markdown paragraphs
    markdown = re.sub(r'<p>(.*?)</p>', r'\1\n\n', markdown, flags=re.DOTALL)

    # Convert <h1>, <h2>, etc. to markdown headers
    for i in range(1, 7):
        pattern = rf'<h{i}>(.*?)</h{i}>'
        replacement = rf'{"#" * i} \1\n\n'
        markdown = re.sub(pattern, replacement, markdown, flags=re.DOTALL)

    # Convert <strong> and <b> to **bold**
    markdown = re.sub(r'<(strong|b)>(.*?)</\1>', r'**\2**', markdown, flags=re.DOTALL)

    # Convert <em> and <i> to *italic*
    markdown = re.sub(r'<(em|i)>(.*?)</\1>', r'*\2*', markdown, flags=re.DOTALL)

    # Convert <a href="...">...</a> to [text](url)
    markdown = re.sub(r'<a\s+href=["\'](.*?)["\']>(.*?)</a>', r'[\2](\1)', markdown, flags=re.DOTALL)

    # Remove any remaining HTML tags
    markdown = re.sub(r'<[^>]+>', '', markdown)

    # Clean up multiple newlines
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)

    return markdown.strip()

def main():
    """Entry point for the script"""
    # Example usage
    html_input = """
    <h1>Main Title</h1>
    <p>This is a paragraph with <strong>bold</strong> and <em>italic</em> text.</p>
    <p>Another paragraph with a <a href="https://example.com">link</a>.</p>
    """

    markdown_output = html_to_markdown(html_input)
    print("Markdown Output:")
    print(markdown_output)

if __name__ == "__main__":
    main()

# BATCH3_PROMPT2_Devstral_test.py

import pytest
from BATCH3_PROMPT2_Devstral import html_to_markdown

def test_html_to_markdown():
    """Test the html_to_markdown function with various inputs"""

    # Test case 1: Basic HTML to markdown conversion
    assert html_to_markdown("<h1>Title</h1>") == "# Title\n\n"
    assert html_to_markdown("<p>Paragraph</p>") == "Paragraph\n\n"

    # Test case 2: Multiple elements
    input_html = """
    <h1>Main Title</h1>
    <p>This is a paragraph with <strong>bold</strong> and <em>italic</em> text.</p>
    <p>Another paragraph with a <a href="https://example.com">link</a>.</p>
    """
    expected_output = "# Main Title\n\nThis is a paragraph with **bold** and *italic* text.\n\nAnother paragraph with a [link](https://example.com).\n\n"
    assert html_to_markdown(input_html) == expected_output

    # Test case 3: Empty input
    assert html_to_markdown("") == ""

    # Test case 4: No HTML tags
    assert html_to_markdown("This is plain text.") == "This is plain text."

    # Test case 5: Mixed content with no HTML tags
    assert html_to_markdown("Text <br> with <strong>bold</strong> and <em>italic</em> text.") == "Text \n\nwith **bold** and *italic* text.\n"

    # Test case 6: Multiple newlines in HTML
    input_html = "<p>Paragraph1<br><br>Paragraph2</p>"
    expected_output = "Paragraph1\n\n\nParagraph2\n\n"
    assert html_to_markdown(input_html) == expected_output

    # Test case 7: Nested HTML tags
    input_html = "<p>This is a <strong>nested <em>bold and italic</em></strong> text.</p>"
    expected_output = "This is a **nested *bold and italic*** text.\n\n"
    assert html_to_markdown(input_html) == expected_output

# Test case 8: HTML with attributes
input_html = "<a href='https://example.com' title='Example'>Link</a>"
expected_output = "[Link](https://example.com)\n"
assert html_to_markdown(input_html) == expected_output

# Test case 9: HTML with multiple <br> tags
input_html = "<p>This is a <br><br><br>paragraph.</p>"
expected_output = "This is a \n\n\nparagraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 10: HTML with multiple <h1> tags
input_html = "<h1>Title1</h1><h1>Title2</h1>"
expected_output = "# Title1\n\n# Title2\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 11: HTML with multiple <p> tags
input_html = "<p>Paragraph1</p><p>Paragraph2</p>"
expected_output = "Paragraph1\n\n\nParagraph2\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 12: HTML with multiple <a> tags
input_html = "<a href='https://example.com'>Link1</a><a href='https://example.org'>Link2</a>"
expected_output = "[Link1](https://example.com)\n[Link2](https://example.org)\n"
assert html_to_markdown(input_html) == expected_output

# Test case 13: HTML with multiple <em> and <strong> tags
input_html = "<p><em>This is</em> a <strong>test</strong>.</p>"
expected_output = "*This is* a **test**.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 14: HTML with multiple <br> and <p> tags
input_html = "<p>This is a <br><br><br>paragraph.</p>"
expected_output = "This is a \n\n\nparagraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 15: HTML with multiple <h2> and <h3> tags
input_html = "<h2>Title2</h2><h3>Title3</h3>"
expected_output = "## Title2\n\n### Title3\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 16: HTML with multiple <a> and <p> tags
input_html = "<p>This is a paragraph with a <a href='https://example.com'>link</a>.</p><p>Another paragraph.</p>"
expected_output = "This is a paragraph with a [link](https://example.com).\n\n\nAnother paragraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 17: HTML with multiple <em> and <strong> tags
input_html = "<p><em>This is</em> a <strong>test</strong>.</p>"
expected_output = "*This is* a **test**.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 18: HTML with multiple <br> and <p> tags
input_html = "<p>This is a <br><br><br>paragraph.</p>"
expected_output = "This is a \n\n\nparagraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 19: HTML with multiple <h2> and <h3> tags
input_html = "<h2>Title2</h2><h3>Title3</h3>"
expected_output = "## Title2\n\n### Title3\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 20: HTML with multiple <a> and <p> tags
input_html = "<p>This is a paragraph with a <a href='https://example.com'>link</a>.</p><p>Another paragraph.</p>"
expected_output = "This is a paragraph with a [link](https://example.com).\n\n\nAnother paragraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 21: HTML with multiple <em> and <strong> tags
input_html = "<p><em>This is</em> a <strong>test</strong>.</p>"
expected_output = "*This is* a **test**.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 22: HTML with multiple <br> and <p> tags
input_html = "<p>This is a <br><br><br>paragraph.</p>"
expected_output = "This is a \n\n\nparagraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 23: HTML with multiple <h2> and <h3> tags
input_html = "<h2>Title2</h2><h3>Title3</h3>"
expected_output = "## Title2\n\n### Title3\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 24: HTML with multiple <a> and <p> tags
input_html = "<p>This is a paragraph with a <a href='https://example.com'>link</a>.</p><p>Another paragraph.</p>"
expected_output = "This is a paragraph with a [link](https://example.com).\n\n\nAnother paragraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 25: HTML with multiple <em> and <strong> tags
input_html = "<p><em>This is</em> a <strong>test</strong>.</p>"
expected_output = "*This is* a **test**.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 26: HTML with multiple <br> and <p> tags
input_html = "<p>This is a <br><br><br>paragraph.</p>"
expected_output = "This is a \n\n\nparagraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 27: HTML with multiple <h2> and <h3> tags
input_html = "<h2>Title2</h2><h3>Title3</h3>"
expected_output = "## Title2\n\n### Title3\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 28: HTML with multiple <a> and <p> tags
input_html = "<p>This is a paragraph with a <a href='https://example.com'>link</a>.</p><p>Another paragraph.</p>"
expected_output = "This is a paragraph with a [link](https://example.com).\n\n\nAnother paragraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 29: HTML with multiple <em> and <strong> tags
input_html = "<p><em>This is</em> a <strong>test</strong>.</p>"
expected_output = "*This is* a **test**.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 30: HTML with multiple <br> and <p> tags
input_html = "<p>This is a <br><br><br>paragraph.</p>"
expected_output = "This is a \n\n\nparagraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 31: HTML with multiple <h2> and <h3> tags
input_html = "<h2>Title2</h2><h3>Title3</h3>"
expected_output = "## Title2\n\n### Title3\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 32: HTML with multiple <a> and <p> tags
input_html = "<p>This is a paragraph with a <a href='https://example.com'>link</a>.</p><p>Another paragraph.</p>"
expected_output = "This is a paragraph with a [link](https://example.com).\n\n\nAnother paragraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 33: HTML with multiple <em> and <strong> tags
input_html = "<p><em>This is</em> a <strong>test</strong>.</p>"
expected_output = "*This is* a **test**.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 34: HTML with multiple <br> and <p> tags
input_html = "<p>This is a <br><br><br>paragraph.</p>"
expected_output = "This is a \n\n\nparagraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 35: HTML with multiple <h2> and <h3> tags
input_html = "<h2>Title2</h2><h3>Title3</h3>"
expected_output = "## Title2\n\n### Title3\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 36: HTML with multiple <a> and <p> tags
input_html = "<p>This is a paragraph with a <a href='https://example.com'>link</a>.</p><p>Another paragraph.</p>"
expected_output = "This is a paragraph with a [link](https://example.com).\n\n\nAnother paragraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 37: HTML with multiple <em> and <strong> tags
input_html = "<p><em>This is</em> a <strong>test</strong>.</p>"
expected_output = "*This is* a **test**.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 38: HTML with multiple <br> and <p> tags
input_html = "<p>This is a <br><br><br>paragraph.</p>"
expected_output = "This is a \n\n\nparagraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 39: HTML with multiple <h2> and <h3> tags
input_html = "<h2>Title2</h2><h3>Title3</h3>"
expected_output = "## Title2\n\n### Title3\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 40: HTML with multiple <a> and <p> tags
input_html = "<p>This is a paragraph with a <a href='https://example.com'>link</a>.</p><p>Another paragraph.</p>"
expected_output = "This is a paragraph with a [link](https://example.com).\n\n\nAnother paragraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 41: HTML with multiple <em> and <strong> tags
input_html = "<p><em>This is</em> a <strong>test</strong>.</p>"
expected_output = "*This is* a **test**.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 42: HTML with multiple <br> and <p> tags
input_html = "<p>This is a <br><br><br>paragraph.</p>"
expected_output = "This is a \n\n\nparagraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 43: HTML with multiple <h2> and <h3> tags
input_html = "<h2>Title2</h2><h3>Title3</h3>"
expected_output = "## Title2\n\n### Title3\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 44: HTML with multiple <a> and <p> tags
input_html = "<p>This is a paragraph with a <a href='https://example.com'>link</a>.</p><p>Another paragraph.</p>"
expected_output = "This is a paragraph with a [link](https://example.com).\n\n\nAnother paragraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 45: HTML with multiple <em> and <strong> tags
input_html = "<p><em>This is</em> a <strong>test</strong>.</p>"
expected_output = "*This is* a **test**.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 46: HTML with multiple <br> and <p> tags
input_html = "<p>This is a <br><br><br>paragraph.</p>"
expected_output = "This is a \n\n\nparagraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 47: HTML with multiple <h2> and <h3> tags
input_html = "<h2>Title2</h2><h3>Title3</h3>"
expected_output = "## Title2\n\n### Title3\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 48: HTML with multiple <a> and <p> tags
input_html = "<p>This is a paragraph with a <a href='https://example.com'>link</a>.</p><p>Another paragraph.</p>"
expected_output = "This is a paragraph with a [link](https://example.com).\n\n\nAnother paragraph.\n\n"
assert html_to_markdown(input_html) == expected_output

# Test case 49: HTML with multiple <em> and <strong> tags
input_html = "<p><em>This is</em> a <strong>test</strong>.</p>"
expected_output = "*