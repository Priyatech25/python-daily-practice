# DAY 36 - Check if Binary Tree is Balanced

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_balance(root):
    if not root:
        return 0

    left = check_balance(root.left)
    if left == -1:
        return -1

    right = check_balance(root.right)
    if right == -1:
        return -1

    if abs(left - right) > 1:
        return -1

    return max(left, right) + 1


def is_balanced(root):
    return check_balance(root) != -1


# Creating tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print("Is Balanced:", is_balanced(root))