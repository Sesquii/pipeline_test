```python
import re

def html_to_markdown(html):
    # Replace headers
    html = re.sub(r'<h[1-6]>', r'#{\1}', html)
    
    # Replace paragraphs
    html = re.sub(r'<p>', '\n\n', html)
    
    # Replace unordered lists
    html = re.sub(r'<ul>', '- \n', html)
    html = re.sub(r'</ul>', '', html)
    
    # Replace list items
    html = re.sub(r'<li>', '* ', html)
    html = re.sub(r'</li>', '', html)
    
    return html

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python BATCH2_PROMPT2_{{model_name}}.py input")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        html = f.read()
    markdown = html_to_markdown(html)
    print(markdown)

# ===== GENERATED TESTS =====
```python
import pytest

# Original code
import re

def html_to_markdown(html):
    # Replace headers
    html = re.sub(r'<h[1-6]>', r'#{\1}', html)
    
    # Replace paragraphs
    html = re.sub(r'<p>', '\n\n', html)
    
    # Replace unordered lists
    html = re.sub(r'<ul>', '- \n', html)
    html = re.sub(r'</ul>', '', html)
    
    # Replace list items
    html = re.sub(r'<li>', '* ', html)
    html = re.sub(r'</li>', '', html)
    
    return html

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python BATCH2_PROMPT2_{{model_name}}.py input")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        html = f.read()
    markdown = html_to_markdown(html)
    print(markdown)

# Test suite
def test_html_to_markdown():
    """Test the html_to_markdown function."""
    
    # Positive test cases
    assert html_to_markdown("<h1>Title</h1>") == "#Title"
    assert html_to_markdown("<p>Paragraph</p>") == "\n\nParagraph\n\n"
    assert html_to_markdown("<ul><li>Item 1</li><li>Item 2</li></ul>") == "- \n* Item 1\n* Item 2"
    
    # Negative test cases
    assert html_to_markdown("<h7>Title</h7>") == "<h7>Title</h7>"
    assert html_to_markdown("<p>Paragraph") == "\n\nParagraph"
    assert html_to_markdown("<ul><li>Item 1<li>Item 2</ul>") == "- \n* Item 1<li>Item 2"

def test_html_to_markdown_with_fixtures():
    """Test the html_to_markdown function using pytest fixtures."""
    
    @pytest.fixture
    def html_data():
        return {
            "<h1>Title</h1>": "#Title",
            "<p>Paragraph</p>": "\n\nParagraph\n\n",
            "<ul><li>Item 1</li><li>Item 2</li></ul>": "- \n* Item 1\n* Item 2"
        }
    
    @pytest.fixture
    def negative_html_data():
        return {
            "<h7>Title</h7>": "<h7>Title</h7>",
            "<p>Paragraph": "\n\nParagraph",
            "<ul><li>Item 1<li>Item 2</ul>": "- \n* Item 1<li>Item 2"
        }
    
    def test_html_to_markdown_with_positive_data(html_data):
        """Test the html_to_markdown function with positive data."""
        for html, expected in html_data.items():
            assert html_to_markdown(html) == expected
    
    def test_html_to_markdown_with_negative_data(negative_html_data):
        """Test the html_to_markdown function with negative data."""
        for html, expected in negative_html_data.items():
            assert html_to_markdown(html) != expected
```