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

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Case 1 and 2: Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: Node with two children
        # Get inorder successor (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's value to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    return root

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=' ')
        inorderTraversal(root.right)

# Example usage
root = None
for k in [20, 10, 30, 5, 15, 25, 35]:
    root = insert(root, k)

print("BST before deletion:")
inorderTraversal(root)

key_to_delete = 10
root = deleteNode(root, key_to_delete)

print(f"\n\nBST after deleting {key_to_delete}:")
inorderTraversal(root)

