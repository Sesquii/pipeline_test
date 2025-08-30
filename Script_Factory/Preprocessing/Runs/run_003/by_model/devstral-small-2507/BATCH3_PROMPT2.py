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