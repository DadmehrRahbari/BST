class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

# Example usage
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

# Build BST
root = None
keys = [10, 5, 15, 3, 7, 12, 18]
for k in keys:
    root = insert(root, k)

print("In-order traversal of BST:")
inorder_traversal(root)
