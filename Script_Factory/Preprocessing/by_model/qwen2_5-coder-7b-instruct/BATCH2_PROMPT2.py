#!/usr/bin/env python3

# BATCH2_PROMPT2_{{model_name}}.py

import re

def reverse_markdown_converter(html_string):
    """
    Converts a formatted HTML string into a simplified markdown format using regular expressions.
    
    Parameters:
    html_string (str): The input HTML or rich-text string to be converted.
    
    Returns:
    str: The converted markdown text.
    """

    # Convert <b> tags to **bold**
    markdown = re.sub(r'<b>(.*?)</b>', r'**\1**', html_string, flags=re.IGNORECASE)
    
    # Convert <i> or <em> tags to *italic*
    markdown = re.sub(r'<i>|<em>', '*', markdown, flags=re.IGNORECASE)
    markdown = re.sub(r'</i>|</em>', '*', markdown, flags=re.IGNORECASE)

    # Convert <u> tags to __underline__
    markdown = re.sub(r'<u>', '__', markdown, flags=re.IGNORECASE)
    markdown = re.sub(r'</u>', '__', markdown, flags=re.IGNORECASE)

    # Convert <a href="...">...</a> tags to [link](url)
    markdown = re.sub(r'<a\s+href="(.*?)">(.*?)</a>', r'[\2](\1)', markdown, flags=re.IGNORECASE)

    # Convert <h[1-6]> tags to ### header ###
    markdown = re.sub(r'<h([1-6])>(.*?)<\/h\1>', lambda m: '#' * int(m.group(1)) + ' ' + m.group(2).strip() + ' #' * int(m.group(1)), markdown, flags=re.IGNORECASE)

    # Convert <p> tags to new lines
    markdown = re.sub(r'<p>(.*?)<\/p>', r'\n\1\n', markdown, flags=re.IGNORECASE)
    
    # Convert <br> tags to new lines
    markdown = re.sub(r'<br\s*/?>', '\n', markdown, flags=re.IGNORECASE)

    return markdown.strip()

if __name__ == "__main__":
    html_input = """
    <h1>Title</h1>
    <p>This is a <b>bold</b> and <i>italic</i> text with <a href="http://example.com">link</a>.</p>
    <p><u>Underline</u> this.</p>
    <h2>Subtitle</h2>
    <br/>
    """
    
    markdown_output = reverse_markdown_converter(html_input)
    print(markdown_output)
```

This Python script defines a function `reverse_markdown_converter` that takes an HTML string as input and converts it into a simplified markdown format using regular expressions. The function handles various HTML tags such as `<b>`, `<i>`, `<u>`, `<a>`, `<h1>` to `<h6>`, `<p>`, and `<br>`. The `if __name__ == "__main__":` block demonstrates how to use the function with a sample HTML input.