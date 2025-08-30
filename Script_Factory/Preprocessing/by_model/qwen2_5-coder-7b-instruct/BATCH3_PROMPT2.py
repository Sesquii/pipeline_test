import re

def reverse_markdown_converter(html_string):
    """
    Converts a formatted HTML or rich-text string into a simplified markdown format using regular expressions.
    
    Args:
    html_string (str): The input HTML or rich-text string to be converted.
    
    Returns:
    str: The converted markdown string.
    """
    # Replace HTML headings with markdown headings
    html_string = re.sub(r'<h([1-6])>(.*?)</h\1>', r'#{\1} \2', html_string)
    
    # Replace HTML paragraphs with markdown paragraphs
    html_string = re.sub(r'<p>(.*?)</p>', r'\1\n\n', html_string)
    
    # Replace HTML bold tags with markdown bold tags
    html_string = re.sub(r'<b>(.*?)</b>', r '**\1**', html_string)
    
    # Replace HTML italics tags with markdown italics tags
    html_string = re.sub(r'<i>(.*?)</i>', r ' *\1*', html_string)
    
    # Replace HTML unordered list items with markdown unordered list items
    html_string = re.sub(r'<li>(.*?)</li>', r' * \1\n', html_string)
    html_string = re.sub(r'<ul>', r'\n', html_string)  # Remove the opening <ul> tag
    html_string = re.sub(r'</ul>', r'\n', html_string)  # Remove the closing </ul> tag
    
    # Replace HTML ordered list items with markdown ordered list items
    html_string = re.sub(r'<ol>', r'\n', html_string)  # Remove the opening <ol> tag
    html_string = re.sub(r'</ol>', r'\n', html_string)  # Remove the closing </ol> tag
    
    # Replace HTML links with markdown links
    html_string = re.sub(r'<a href="(.*?)">(.*?)</a>', r' [\2](\1)', html_string)
    
    return html_string.strip()

# Entry point for the script
if __name__ == "__main__":
    # Example usage
    html_input = """
    <h1>Title</h1>
    <p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>
    <ol>
        <li>Ordered Item 1</li>
        <li>Ordered Item 2</li>
    </ol>
    <a href="https://example.com">Link</a>
    """
    
    markdown_output = reverse_markdown_converter(html_input)
    print(markdown_output)