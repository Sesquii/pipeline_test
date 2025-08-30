```python
import re

def html_to_markdown(html):
    # Convert paragraph tags to empty string (content is preserved)
    html = re.sub(r'<p>', '', html)
    html = re.sub(r'</p>', '', html)

    # Convert bold tags to **bold**
    html = re.sub(r'<b>', '**', html)
    html = re.sub(r'</b>', '', html)

    # Convert italic tags to *italic*
    html = re.sub(r'<i>', '*', html)
    html = re.sub(r'</i>', '', html)

    # Convert links to [link](url)
    html = re.sub(r'<a\s+href="([^"]+)">', r'[link](\1)', html)
    html = re.sub(r'</a>', '', html)

    # Convert strong tags to **strong**
    html = re.sub(r'<strong>', '**', html)
    html = re.sub(r'</strong>', '', html)

    # Convert emphasis tags to *emphasis*
    html = re.sub(r'<em>', '*', html)
    html = re.sub(r'</em>', '', html)

    return html

if __name__ == "__main__":
    input_html = "<p>Hello <b>world</b></p>"
    output_md = html_to_markdown(input_html)
    print(output_md)