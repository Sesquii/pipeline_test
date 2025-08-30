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