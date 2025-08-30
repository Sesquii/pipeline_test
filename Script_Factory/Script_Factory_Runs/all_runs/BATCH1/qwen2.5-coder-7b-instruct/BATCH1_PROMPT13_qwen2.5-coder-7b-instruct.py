import random

UNHELPFUL_COMMENTS = [
    "good stuff here",
    "fix maybe",
    "nice work",
    "this is a good place",
    "maybe not needed",
    "keep it simple",
    "refactor this",
    "what was I thinking?",
    "why did I write this?",
    "delete me if you don't need me"
]

def add_unhelpful_comments(code: str) -> str:
    tree = ast.parse(code)
    visitor = CommentInsertionVisitor()
    visitor.visit(tree)
    return ast.unparse(tree)

class CommentInsertionVisitor(ast.NodeTransformer):
    def generic_visit(self, node):
        super().generic_visit(node)
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            self.insert_comment_before_node(node)
        else:
            self.insert_comment_after_node(node)
        return node

    def insert_comment_before_node(self, node):
        comment = f'# {random.choice(UNHELPFUL_COMMENTS)}'
        new_node = ast.Expr(value=ast.Str(s=comment))
        node.body.insert(0, new_node)

    def insert_comment_after_node(self, node):
        if not isinstance(node, (ast.Module, ast.Expr)):
            comment = f'# {random.choice(UNHELPFUL_COMMENTS)}'
            new_node = ast.Expr(value=ast.Str(s=comment))
            node.body.append(new_node)

if __name__ == "__main__":
    example_code = """
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
"""
    commented_code = add_unhelpful_comments(example_code)
    print(commented_code)