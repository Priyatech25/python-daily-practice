# DAY 32 - DSA Practice (Inorder Traversal)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    
    inorder(root.left)        # Left
    print(root.val, end=" ")  # Root
    inorder(root.right)       # Right


# Creating tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder Traversal:")
inorder(root)