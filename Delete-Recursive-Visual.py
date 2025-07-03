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
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    return root

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=' ')
        inorderTraversal(root.right)

def print_tree(root):
    def _build(node):
        if node is None:
            return [], 0, 0

        label = str(node.val)
        label_width = len(label)

        if node.left is None and node.right is None:
            return [label], label_width, label_width // 2

        left_lines, left_w, left_root = _build(node.left)
        right_lines, right_w, right_root = _build(node.right)

        gap = 2
        first_line = (
            " " * left_w + label + " " * (right_w + gap - label_width)
        )

        second_line_left = (
            " " * left_root + "/" + " " * (left_w - left_root - 1)
            if node.left else " " * left_w
        )
        second_line_right = (
            " " * right_root + "\\" + " " * (right_w - right_root - 1)
            if node.right else " " * right_w
        )
        second_line = second_line_left + " " * gap + second_line_right

        max_child_height = max(len(left_lines), len(right_lines))
        left_lines += [" " * left_w] * (max_child_height - len(left_lines))
        right_lines += [" " * right_w] * (max_child_height - len(right_lines))

        merged_children = [
            l + " " * gap + r for l, r in zip(left_lines, right_lines)
        ]

        return [first_line, second_line] + merged_children, \
               left_w + gap + right_w, \
               left_w + gap // 2

    lines, _, _ = _build(root)
    for line in lines:
        print(line.rstrip())

# Example usage
root = None
for k in [20, 10, 30, 5, 15, 25, 35]:
    root = insert(root, k)

print("BST before deletion:")
print_tree(root)

print("\nIn-order traversal before deletion:")
inorderTraversal(root)
print()

key_to_delete = 10
root = deleteNode(root, key_to_delete)

print(f"\nBST after deleting {key_to_delete}:")
print_tree(root)

print("\nIn-order traversal after deletion:")
inorderTraversal(root)
print()
