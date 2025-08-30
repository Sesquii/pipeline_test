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