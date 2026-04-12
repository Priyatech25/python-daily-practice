# DAY 37 - Diameter of Binary Tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diameter_of_tree(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        if not node:
            return 0
        
        left = height(node.left)
        right = height(node.right)

        # Update diameter
        diameter = max(diameter, left + right)

        return max(left, right) + 1

    height(root)
    return diameter


# Creating tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Diameter of Tree:", diameter_of_tree(root))