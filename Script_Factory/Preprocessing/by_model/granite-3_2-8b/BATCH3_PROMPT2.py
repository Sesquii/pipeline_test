# BATCH3_PROMPT2_Granite.py

import re

def html_to_markdown(html):
    """
    Converts HTML to simplified Markdown using regular expressions.

    :param html: A string containing HTML or rich-text formatting.
    :return: A string representing the equivalent Markdown.
    """

    # Bold text: <strong> and </strong>, or <b> and </b>
    markdown_bold = re.sub(r'<(strong|b)>(.*?)</(\1)>', r'**\2**', html, flags=re.DOTALL)

    # Italic text: <em> and </em>, or <i> and </i>
    markdown_italic = re.sub(r'<(em|i)>(.*?)</(\1)>', r'*\2*', html, flags=re.DOTALL)

    # Headings: h1-h6 are converted to #-###### respectively
    markdown_heading = re.sub(r'^(<h[1-6])(.*?)(</\2>)$', r'#\2', markdown_bold + markdown_italic, flags=re.MULTILINE | re.DOTALL)

    # Unordered lists: <ul> and </ul>, with <li> elements inside
    markdown_list = re.sub(r'<ul>(.*?)</ul>', r'\1\n', markdown_heading)
    list_items = re.findall(r'<li>(.*?)</li>', markdown_list, flags=re.DOTALL)
    markdown_list = re.sub(r'<ul>(.*?)</ul>', '- ' + '\n- '.join(list_items) + '\n', markdown_list, flags=re.MULTILINE | re.DOTALL)

    # Links: <a href="..."> and </a>
    markdown_link = re.sub(r'<a\s+(?:(?!href).)*?\bhref=(["\'])(.*?)\1[^>]*>(.*?)</a>', r'[\2](\3)', markdown_list)

    # Paragraphs: text between <p> and </p>, or just line breaks
    paragraphs = re.split(r'<(p|br)/?>', markdown_link)
    markdown_paragraphs = [p for p in paragraphs if p]  # Remove empty strings

    return '\n'.join(markdown_paragraphs)


if __name__ == "__main__":
    html_input = """
    <h1>Header 1</h1>
    <strong>Bold text</strong> and <em>italic text</em>.
    <ul>
        <li><a href="https://example.com">Link</a></li>
    </ul>
    Paragraph with some <b>bold</b> and <i>italic</i> parts.
    """

    markdown_output = html_to_markdown(html_input)
    print(markdown_output)