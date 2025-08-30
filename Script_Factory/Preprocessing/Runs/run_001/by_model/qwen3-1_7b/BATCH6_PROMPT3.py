```python
class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def generate_dungeon():
    root = Node("Main Room")
    left_child, right_child = split(root)
    left_left, left_right = split(left_child)
    right_left, right_right = split(right_child)
    return root

def split(node):
    left = Node("Left Child")
    right = Node("Right Child")
    node.left = left
    node.right = right
    return left, right

def visualize(node):
    print(f"{node.name}")
    if node.left:
        print("~", end="")
        visualize(node.left)
    if node.right:
        print("~", end="")
        visualize(node.right)

if __name__ == "__main__":
    dungeon = generate_dungeon()
    visualize(dungeon)