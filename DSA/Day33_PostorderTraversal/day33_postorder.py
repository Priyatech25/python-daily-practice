# DAY 33 - DSA Practice (Postorder Traversal)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder(root):
    if not root:
        return
    
    postorder(root.left)      # Left
    postorder(root.right)     # Right
    print(root.val, end=" ")  # Root


# Creating tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Postorder Traversal:")
postorder(root)