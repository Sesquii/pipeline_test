```python
import random

def add_unhelpful_comments(code: str) -> str:
    comments = ["good stuff here", "fix maybe", "nice work"]
    num_comments = 2
    result = []
    
    for _ in range(num_comments):
        comment = random.choice(comments)
        pos = random.randint(0, len(code))
        new_code = code[:pos] + comment + code[pos:]
        result.append(new_code)
    
    return ''.join(result)

if __name__ == "__main__":
    example_code = """
def greet(name):
    print(f"Hello, {name}!")
"""
    modified_code = add_unhelpful_comments(example_code)
    print(modified_code)