import random
import re
import ast
import tokenize
from io import StringIO

def add_unhelpful_comments(code: str) -> str:
    # Parse the code to get AST
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return code  # Return original if syntax is invalid
    
    # Get all statement positions
    statements = []
    
    def collect_statements(node, parent=None):
        if isinstance(node, ast.stmt):
            # Get the line number and column of the statement
            lineno = getattr(node, 'lineno', None)
            col_offset = getattr(node, 'col_offset', None)
            if lineno is not None:
                statements.append((lineno, col_offset, node))
        
        for child in ast.iter_child_nodes(node):
            collect_statements(child, node)
    
    collect_statements(tree)
    
    # Sort by line number
    statements.sort(key=lambda x: x[0])
    
    # Split code into lines
    lines = code.split('\n')
    
    # Get token positions to avoid placing comments in inappropriate places
    tokens = []
    try:
        for tok in tokenize.generate_tokens(StringIO(code).readline):
            if tok.type == tokenize.OP or tok.type == tokenize.NAME or tok.type == tokenize.NUMBER or tok.type == tokenize.STRING:
                tokens.append((tok.start[0], tok.end[0], tok.start[1], tok.end[1], tok.string))
    except:
        pass  # If tokenization fails, proceed without it
    
    # Unhelpful comments to insert
    unhelpful_comments = [
        "good stuff here",
        "fix maybe",
        "nice work",
        "this is important",
        "what does this do?",
        "look at this",
        "very clever",
        "needs improvement",
        "review this",
        "this might break",
        "check this out",
        "interesting approach",
        "this could be better",
        "not sure about this",
        "needs more work",
        "this is weird",
        "what am I doing?",
        "oh no, another one",
        "this looks wrong",
        "maybe this works"
    ]
    
    # Track which lines already have comments
    lines_with_comments = set()
    
    # Insert comments at random positions
    new_lines = lines[:]
    num_insertions = max(1, len(statements) // 3)  # Insert about 1/3 of statements
    
    # Try to insert comments near statements but avoid placing them in the middle of tokens
    for _ in range(num_insertions):
        if not statements:
            break
            
        # Pick a random statement
        lineno, col_offset, node = random.choice(statements)
        
        # Adjust line number (1-based vs 0-based)
        line_idx = lineno - 1
        
        # Skip if this line already has a comment or is out of bounds
        if line_idx >= len(new_lines) or line_idx in lines_with_comments:
            continue
            
        # Determine where to insert: before, after, or inside the statement
        if random.random() < 0.5:
            # Insert before the statement
            comment = random.choice(unhelpful_comments)
            if col_offset is not None and col_offset > 0:
                # Insert at the beginning of line with proper indentation
                indent = len(new_lines[line_idx]) - len(new_lines[line_idx].lstrip())
                new_lines[line_idx] = ' ' * indent + '# ' + comment + '\n' + new_lines[line_idx]
            else:
                new_lines[line_idx] = '# ' + comment + '\n' + new_lines[line_idx]
        else:
            # Insert after the statement
            comment = random.choice(unhelpful_comments)
            if line_idx < len(new_lines) - 1:
                # Insert a comment on the next line with same indentation
                indent = len(new_lines[line_idx]) - len(new_lines[line_idx].lstrip())
                new_lines.insert(line_idx + 1, ' ' * indent + '# ' + comment)
            else:
                # If at end, add comment at the end
                new_lines.append('# ' + comment)
        
        lines_with_comments.add(line_idx)
    
    # Ensure we still have valid Python code by making sure indentation is correct
    # and we don't break the structure
    
    # Also add some comments randomly in non-statement positions
    num_additional = random.randint(0, max(2, len(lines) // 4))
    for _ in range(num_additional):
        line_idx = random.randint(0, len(new_lines) - 1)
        if new_lines[line_idx].strip() and not new_lines[line_idx].strip().startswith('#'):
            comment = random.choice(unhelpful_comments)
            indent = len(new_lines[line_idx]) - len(new_lines[line_idx].lstrip())
            new_lines[line_idx] = ' ' * indent + '# ' + comment + '\n' + new_lines[line_idx]
    
    # Clean up the result to avoid double comments
    final_lines = []
    for line in new_lines:
        if line.strip() and line.lstrip().startswith('#'):
            # Check if there's already a comment on this line
            final_lines.append(line)
        elif line.strip():
            final_lines.append(line)
    
    return '\n'.join(final_lines)

# Example usage
if __name__ == "__main__":
    sample_code = """
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    for i in range(10):
        print(fibonacci(i))

if __name__ == "__main__":
    main()
"""
    
    print("Original code:")
    print(sample_code)
    print("\nCode with unhelpful comments:")
    print(add_unhelpful_comments(sample_code))
