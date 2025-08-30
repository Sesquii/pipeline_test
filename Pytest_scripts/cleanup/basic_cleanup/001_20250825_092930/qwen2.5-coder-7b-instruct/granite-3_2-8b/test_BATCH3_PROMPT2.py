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

# ===== GENERATED TESTS =====
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
    markdown_italic = re.sub(r'<(em|i)>(.*?)</(\1)>', r'*\2*', markdown_bold + markdown_italic, flags=re.DOTALL)

    # Headings: h1-h6 are converted to #-###### respectively
    markdown_heading = re.sub(r'^(<h[1-6])(.*?)(</\2>)$', r'#\2', markdown_italic, flags=re.MULTILINE | re.DOTALL)

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


# BATCH3_PROMPT2_Granite_test.py

import pytest
from BATCH3_PROMPT2_Granite import html_to_markdown

@pytest.fixture
def sample_html():
    return """
    <h1>Header 1</h1>
    <strong>Bold text</strong> and <em>italic text</em>.
    <ul>
        <li><a href="https://example.com">Link</a></li>
    </ul>
    Paragraph with some <b>bold</b> and <i>italic</i> parts.
    """

@pytest.fixture
def expected_markdown():
    return """
#Header 1

**Bold text** and *italic text*.

- [https://example.com](Link)

Paragraph with some **bold** and *italic* parts.
"""

def test_html_to_markdown(sample_html: str, expected_markdown: str):
    assert html_to_markdown(sample_html) == expected_markdown.strip()

def test_html_to_markdown_empty_input():
    assert html_to_markdown("") == ""

def test_html_to_markdown_no_tags():
    assert html_to_markdown("No HTML tags here.") == "No HTML tags here."

def test_html_to_markdown_all_tags():
    html = """
    <h1>Header 1</h1>
    <strong>Bold text</strong> and <em>italic text</em>.
    <ul>
        <li><a href="https://example.com">Link</a></li>
    </ul>
    Paragraph with some <b>bold</b> and <i>italic</i> parts.
    """
    markdown = """
#Header 1

**Bold text** and *italic text*.

- [https://example.com](Link)

Paragraph with some **bold** and *italic* parts.
"""
    assert html_to_markdown(html) == markdown.strip()

def test_html_to_markdown_mixed_tags():
    html = """
    <h2>Header 2</h2>
    <p>This is a paragraph.</p>
    <ul>
        <li><a href="https://example.com">Link</a></li>
        <li><a href="https://example.org">Another Link</a></li>
    </ul>
    """
    markdown = """
##Header 2

This is a paragraph.

- [https://example.com](Link)
- [https://example.org](Another Link)
"""
    assert html_to_markdown(html) == markdown.strip()

def test_html_to_markdown_invalid_tags():
    html = """
    <h1>Header 1</h1>
    <strong>Bold text</strong> and <em>italic text</em>.
    <ul>
        <li><a href="https://example.com">Link</a></li>
    </ul>
    Paragraph with some <b>bold</b> and <i>italic</i> parts.
    """
    markdown = """
#Header 1

**Bold text** and *italic text*.

- [https://example.com](Link)

Paragraph with some **bold** and *italic* parts.
"""
    assert html_to_markdown(html) == markdown.strip()

def test_html_to_markdown_with_br_tags():
    html = """
    <p>This is a paragraph.<br>With line breaks.</p>
    """
    markdown = """
This is a paragraph.

With line breaks.
"""
    assert html_to_markdown(html) == markdown.strip()
