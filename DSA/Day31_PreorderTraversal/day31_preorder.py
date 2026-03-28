# DAY 31 - DSA Practice (Preorder Traversal)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root):
    if not root:
        return
    
    print(root.val, end=" ")   # Visit root
    preorder(root.left)        # Left
    preorder(root.right)       # Right


# Creating tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder Traversal:")
preorder(root)