class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

# ─────────────────────────────
# Insertion (from previous step)
# ─────────────────────────────
def bst_insert(root, z):
    y = None
    x = root
    while x is not None:
        y = x
        x = x.left if z.key < x.key else x.right
    z.parent = y
    if y is None:
        return z               # tree was empty
    if z.key < y.key:
        y.left = z
    else:
        y.right = z
    return root

# ────────────────
# Helper utilities
# ────────────────
def tree_minimum(node):
    while node.left is not None:
        node = node.left
    return node

def tree_successor(node):
    if node.right:
        return tree_minimum(node.right)
    y = node.parent
    while y is not None and node is y.right:
        node = y
        y = y.parent
    return y

# ────────────────────────────────
# Deletion node
# ────────────────────────────────
def bst_delete(root, z):
    # Step 1: choose y
    if z.left is None or z.right is None:
        y = z
    else:
        y = tree_successor(z)

    # Step 2: choose x
    x = y.left if y.left is not None else y.right

    # Step 3: splice out y
    if x is not None:
        x.parent = y.parent

    if y.parent is None:
        root = x                       # y was the root
    elif y is y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x

    # Step 4: copy y’s key/data into z (if we didn’t really delete z)
    if y is not z:
        z.key = y.key
        # copy any other satellite data fields here

    return root        # new root may have changed

# ─────────────────────
# In‑order traversal
# ─────────────────────
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=' ')
        inorder_traversal(node.right)

# ───────────────
# Demo / test run
# ───────────────
if __name__ == "__main__":
    # Build a sample tree
    root = None
    for value in [15, 6, 18, 3, 7, 17, 20]:
        root = bst_insert(root, Node(value))

    print("Before delete:")
    inorder_traversal(root)       # 3 6 7 15 17 18 20
    print()

    # Delete node with key 6
    # (simple search loop just for the demo)
    node = root
    while node and node.key != 6:
        node = node.left if 6 < node.key else node.right

    if node:
        root = bst_delete(root, node)

    print("After delete:")
    inorder_traversal(root)       # 3 7 15 17 18 20
    print()
