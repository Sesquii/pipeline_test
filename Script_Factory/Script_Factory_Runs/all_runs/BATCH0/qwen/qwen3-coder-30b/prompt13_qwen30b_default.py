import ast
import random
import re

def add_unhelpful_comments(code: str) -> str:
    if not code.strip():
        return code
    
    # Parse the code to get AST
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return code  # Return original if syntax is invalid
    
    # Extract all statement positions (line number, start column, end column)
    statements = []
    
    def walk(node, parent=None):
        if isinstance(node, ast.stmt):
            # Get line numbers for the node
            if hasattr(node, 'lineno') and hasattr(node, 'end_lineno'):
                start_line = node.lineno
                end_line = node.end_lineno or node.lineno
                
                # Get column info if available
                start_col = getattr(node, 'col_offset', 0)
                end_col = getattr(node, 'end_col_offset', None)
                
                statements.append((start_line, end_line, start_col, end_col, node))
        
        for child in ast.iter_child_nodes(node):
            walk(child, node)
    
    walk(tree)
    
    # Extract lines from code
    lines = code.split('\n')
    
    # Create a list of all possible comment insertion points
    comment_points = []
    
    # Add points before statements
    for start_line, end_line, start_col, end_col, node in statements:
        if start_line <= len(lines):
            comment_points.append(('before', start_line - 1, start_col))
    
    # Add points after statements
    for start_line, end_line, start_col, end_col, node in statements:
        if end_line < len(lines):
            comment_points.append(('after', end_line, 0))
    
    # Add points inside function definitions (before first statement)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.body:
            first_stmt = node.body[0]
            if hasattr(first_stmt, 'lineno'):
                line_num = first_stmt.lineno - 1
                comment_points.append(('inside', line_num, 0))
    
    # Add points inside class definitions (before first statement)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.body:
            first_stmt = node.body[0]
            if hasattr(first_stmt, 'lineno'):
                line_num = first_stmt.lineno - 1
                comment_points.append(('inside', line_num, 0))
    
    # Add points inside loops (before first statement)
    for node in ast.walk(tree):
        if isinstance(node, (ast.For, ast.While)) and node.body:
            first_stmt = node.body[0]
            if hasattr(first_stmt, 'lineno'):
                line_num = first_stmt.lineno - 1
                comment_points.append(('inside', line_num, 0))
    
    # Add points before imports
    for i, line in enumerate(lines):
        if re.match(r'^\s*(import|from)\s', line):
            comment_points.append(('before', i, 0))
    
    # Filter out duplicates and sort by position
    unique_points = list(set(comment_points))
    unique_points.sort(key=lambda x: (x[1], x[2]))
    
    # Select random points to add comments
    unhelpful_comments = [
        "good stuff here",
        "fix maybe", 
        "nice work",
        "this is important",
        "what does this do?",
        "maybe this needs fixing",
        "interesting approach",
        "check this out",
        "needs more work",
        "this looks good",
        "is this right?",
        "could be better",
        "comment needed here",
        "functionality here",
        "optimization point",
        "code review needed",
        "this is tricky",
        "watch out here",
        "review this logic",
        "important section"
    ]
    
    # Shuffle the comment points and add comments
    random.shuffle(unique_points)
    
    # Add comments to a subset of points (about 1/3 of total points)
    num_comments = max(1, len(unique_points) // 3)
    selected_points = unique_points[:num_comments]
    
    # Sort in reverse order so we don't mess up line numbers
    selected_points.sort(reverse=True)
    
    lines_copy = lines[:]
    
    for point_type, line_num, col in selected_points:
        if line_num < len(lines_copy):
            comment = random.choice(unhelpful_comments)
            
            if point_type == 'before':
                # Add comment before the line
                current_line = lines_copy[line_num]
                indent = re.match(r'^\s*', current_line).group()
                lines_copy[line_num] = f"{indent}# {comment}\n{current_line}"
                
            elif point_type == 'after':
                # Add comment after the line (insert new line)
                current_line = lines_copy[line_num]
                indent = re.match(r'^\s*', current_line).group()
                lines_copy.insert(line_num + 1, f"{indent}# {comment}")
                
            elif point_type == 'inside':
                # Add comment inside a statement block
                current_line = lines_copy[line_num]
                indent = re.match(r'^\s*', current_line).group()
                if not current_line.strip().startswith('#'):
                    lines_copy[line_num] = f"{current_line}{indent}# {comment}"
    
    return '\n'.join(lines_copy)

if __name__ == "__main__":
    # Example code snippet
    sample_code = '''
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    data = [1, 2, 3, 4, 5]
    result = calculate_sum(data)
    print(f"Sum is: {result}")

if __name__ == "__main__":
    main()
'''
    
    print("Original code:")
    print(sample_code)
    print("\n" + "="*50 + "\n")
    
    commented_code = add_unhelpful_comments(sample_code)
    print("Code with unhelpful comments:")
    print(commented_code)
