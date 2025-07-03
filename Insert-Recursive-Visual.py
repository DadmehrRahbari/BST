class TreeNode:
    def __init__(self, key):
        self.val   = key
        self.left  = None
        self.right = None

# ---------- BST core operations ----------
def insert(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

# ---------- Plain-text vertical printer ----------
def print_tree(root):

    def _build(node):

        if node is None:
            return [], 0, 0

        label      = str(node.val)
        label_width = len(label)

        # Leaf — just the label
        if node.left is None and node.right is None:
            return [label], label_width, label_width // 2

        # Build left and right sub-blocks
        left_lines,  left_w,  left_root  = _build(node.left)
        right_lines, right_w, right_root = _build(node.right)

        gap = 2  # spaces between left and right blocks
        first_line = (
            " " * left_w + label + " " * (right_w + gap - label_width)
        )

        # Branch connectors
        second_line_left = (
            " " * left_root + "/" + " " * (left_w - left_root - 1)
            if node.left else " " * left_w
        )
        second_line_right = (
            " " * right_root + "\\" + " " * (right_w - right_root - 1)
            if node.right else " " * right_w
        )
        second_line = second_line_left + " " * gap + second_line_right

        # Pad shorter subtree with empty lines
        max_child_height = max(len(left_lines), len(right_lines))
        left_lines  += [" " * left_w]  * (max_child_height - len(left_lines))
        right_lines += [" " * right_w] * (max_child_height - len(right_lines))

        merged_children = [
            l + " " * gap + r for l, r in zip(left_lines, right_lines)
        ]

        return [first_line, second_line] + merged_children, \
               left_w + gap + right_w, \
               left_w + gap // 2

    # Build and print
    lines, _, _ = _build(root)
    for ln in lines:
        print(ln.rstrip())

# ---------- Demo ----------
if __name__ == "__main__":
    # Build BST
    root = None
    keys = [10, 5, 15, 3, 7, 12, 18]
    for k in keys:
        root = insert(root, k)

    # In-order verification
    print("In-order traversal of BST:")
    inorder_traversal(root)
    print("\n")

    # Visual representation
    print("Tree view:")
    print_tree(root)

