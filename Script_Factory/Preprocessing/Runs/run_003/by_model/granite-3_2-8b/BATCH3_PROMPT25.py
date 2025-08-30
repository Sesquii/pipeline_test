import ast
import random

UNRELATED_COMMENTS = [
    "This comment is completely unrelated.",
    "Here's a random fact: An octopus has three hearts.",
    "Did you know that a group of flamingos is called a 'flamboyance'?",
    "Remember, always brush your teeth for at least two minutes.",
    "The square root of -1 is my favorite number.",
]

ABSURD_COMMENTS = [
    ("print('Hello World')", "This line prints the greeting to the dawn, symbolizing hope and a new beginning."),
    ("x = 5", "Assigning the value five to variable x, a prime number often associated with growth and stability in numerology."),
    ("if x > 10:", "Checking if the variable x surpasses ten units, a number symbolic of completeness in many cultures."),
]


def generate_comment(node):
    if isinstance(node, ast.Print):
        return random.choice([UNRELATED_COMMENTS[random.randint(0, len(UNRELATED_COMMENTS) - 1)],
                              next(absurd for absurd, _ in ABSURD_COMMENTS if node.value.id == absurd[0])])
    elif isinstance(node, ast.Assign):
        return random.choice([UNRELATED_COMMENTS[random.randint(0, len(UNRELATED_COMMENTS) - 1)],
                              next(absurd for absurd, _ in ABSURD_COMMENTS if node.targets[0].id == absurd[0])])
    elif isinstance(node, ast.If):
        return random.choice([UNRELATED_COMMENTS[random.randint(0, len(UNRELATED_COMMENTS) - 1)],
                              next(absurd for absurd, _ in ABSURD_COMMENTS if node.test.id == absurd[0])])
    else:
        return UNRELATED_COMMENTS[random.randint(0, len(UNRELATED_COMMENTS) - 1)]


def insert_comments(code):
    tree = ast.parse(code)

    for node in ast.walk(tree):
        if hasattr(node, 'body'):
            node.body.append(ast.Comment(generate_comment(node)))
        elif hasattr(node, 'value'):
            node.value.comment = generate_comment(node)

    return ast.unparse(tree)


if __name__ == "__main__":
    with open("input_code.py", "r") as file:
        code = file.read()
    
    commented_code = insert_comments(code)
    with open("output_code.py", "w") as file:
        file.write(commented_code)

    print("Code comments have been inserted successfully.")