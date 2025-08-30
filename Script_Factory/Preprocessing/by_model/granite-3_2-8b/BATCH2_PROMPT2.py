import re

def html_to_markdown(html):
    """
    Converts HTML to simplified Markdown using regular expressions.

    Args:
        html (str): Input string in HTML or rich-text format.

    Returns:
        str: Markdown formatted string.
    """

    # Headers
    html = re.sub(r'^(#+) (.*)$', r'\1 \2', html, flags=re.MULTILINE)
    
    # Bold and Italic
    html = re.sub(r'(\*\*)(.+?)\*(\\*)', r'<b>\2</b>', html)  # Bold
    html = re.sub(r'(\\*)(.*?)\\*', r'<i>\1\2</i>', html)     # Italic

    # Lists
    html = re.sub(r'^(-|\*|\+) (.*?)(?=$|^(-|\*|\+))', r'\1. \2', html, flags=re.MULTILINE | re.DOTALL)
    
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'[\\b\1\\e]', html)  # Basic link

    # Images
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'![\\i\1\\e\\](\2)', html)  # Image

    # Code blocks
    html = re.sub(r'`{3}(.*?)`{3}', r'<code>\1</code>', html, flags=re.DOTALL)
    
    return html

if __name__ == "__main__":
    # Test HTML input
    html_input = """
    # Header 1
    **Bold text** and *Italic text*.

    - Unordered list item
    - Another item

    [Link Text](https://www.example.com)

    ![Image Alt Text](image.jpg)

    ```
    Code block
    ```
    """

    markdown_output = html_to_markdown(html_input)
    print(markdown_output)