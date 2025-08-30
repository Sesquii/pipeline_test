import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from Script_Factory.Script_Factory_Runs.all_runs.BATCH2.granite-3.2-8b.BATCH2_PROMPT2_granite-3.2-8b import (
    html_to_markdown,
    rich_text_to_markdown
)

import pytest

def test_html_to_markdown_normal():
    """Test normal HTML to Markdown conversion."""
    input_html = "# Header\n* List item 1\n* List item 2"
    expected_output = "\\# Header\n\\* List item 1\n\\* List item 2"
    assert html_to_markdown(input_html) == expected_output

def test_html_to_markdown_edge_case_empty():
    """Test HTML to Markdown conversion with an empty string."""
    input_html = ""
    expected_output = ""
    assert html_to_markdown(input_html) == expected_output

def test_html_to_markdown_edge_case_null():
    """Test HTML to Markdown conversion with None."""
    input_html = None
    with pytest.raises(TypeError):
        html_to_markdown(input_html)

def test_rich_text_to_markdown_normal():
    """Test normal rich text to Markdown conversion."""
    input_rt = "**Bold** *Italic* __Underlined__"
    expected_output = "**Bold** *Italic* __Underlined__"
    assert rich_text_to_markdown(input_rt) == expected_output

def test_rich_text_to_markdown_edge_case_empty():
    """Test rich text to Markdown conversion with an empty string."""
    input_rt = ""
    expected_output = ""
    assert rich_text_to_markdown(input_rt) == expected_output

def test_rich_text_to_markdown_edge_case_null():
    """Test rich text to Markdown conversion with None."""
    input_rt = None
    with pytest.raises(TypeError):
        rich_text_to_markdown(input_rt)

if __name__ == "__main__":
    pytest.main()