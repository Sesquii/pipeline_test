import random

class BSPNode:
    def __init__(self, rect):
        self.rect = rect
        self.left = None
        self.right = None

def split_node(node):
    if node.rect.height > node.rect.width:
        # Split vertically
        split_y = node.rect.y + random.randint(0, node.rect.height - 2)
        node.left = BSPNode(Rectangle(node.rect.x, node.rect.y, node.rect.width, split_y - node.rect.y))
        node.right = BSPNode(Rectangle(node.rect.x, split_y + 1, node.rect.width, node.rect.bottom - split_y - 1))
    else:
        # Split horizontally
        split_x = node.rect.x + random.randint(0, node.rect.width - 2)
        node.left = BSPNode(Rectangle(node.rect.x, node.rect.y, split_x - node.rect.x, node.rect.height))
        node.right = BSPNode(Rectangle(split_x + 1, node.rect.y, node.rect.right - split_x - 1, node.rect.height))

def draw_dungeon(root, dungeon_map):
    if root is None:
        return
    x1, y1 = root.rect.x, root.rect.y
    x2, y2 = root.rect.right, root.rect.bottom
    for x in range(x1 + 1, x2):
        dungeon_map[y1][x] = '#'
        dungeon_map[y2][x] = '#'
    for y in range(y1 + 1, y2):
        dungeon_map[y][x1] = '#'
        dungeon_map[y][x2] = '#'
    draw_dungeon(root.left, dungeon_map)
    draw_dungeon(root.right, dungeon_map)

def connect_nodes(node1, node2, dungeon_map):
    if node1 is None or node2 is None:
        return
    x1, y1 = node1.rect.x + node1.rect.width // 2, node1.rect.y + node1.rect.height // 2
    x2, y2 = node2.rect.x + node2.rect.width // 2, node2.rect.y + node2.rect.height // 2
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    
    if dx > dy:
        step_x = (x2 - x1) / dx
        for _ in range(dx):
            dungeon_map[min(max(int(y1), 0), len(dungeon_map) - 1)][min(max(int(x1 + step_x * i), 0), len(dungeon_map[0]) - 1)] = '~'
            x1 += step_x
    else:
        step_y = (y2 - y1) / dy
        for _ in range(dy):
            dungeon_map[min(max(int(y1 + step_y * i), 0), len(dungeon_map) - 1)][min(max(int(x1), 0), len(dungeon_map[0]) - 1)] = '~'
            y1 += step_y

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.right = x + width - 1
        self.bottom = y + height - 1

if __name__ == "__main__":
    width, height = 20, 20
    dungeon_map = [[' ' for _ in range(width)] for _ in range(height)]
    
    root = BSPNode(Rectangle(0, 0, width, height))
    stack = [root]
    
    while stack:
        node = stack.pop()
        if random.randint(0, 1) == 0 and node.rect.width > 2 and node.rect.height > 2:
            split_node(node)
            stack.extend([node.left, node.right])
    
    draw_dungeon(root, dungeon_map)
    for row in dungeon_map:
        print(''.join(row))
    
    # Connect all rooms
    connect_nodes(root.left, root.right, dungeon_map)
    connect_nodes(root.left.left, root.left.right, dungeon_map)
    connect_nodes(root.right.left, root.right.right, dungeon_map)
    
    for row in dungeon_map:
        print(''.join(row))