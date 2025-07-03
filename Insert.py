class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def bst_insert(root, z):
    y = None
    x = root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y is None:
        root = z  # Tree was empty
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    return root

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=' ')
        inorder_traversal(node.right)

# Create nodes
root = None
values = [15, 6, 18, 3, 7, 17, 20]

for val in values:
    node = Node(val)
    root = bst_insert(root, node)

inorder_traversal(root)
