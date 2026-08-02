"""
Day 49 - Validate Binary Search Tree

Problem:
Given the root of a binary tree,
determine whether it is a valid
Binary Search Tree (BST).

A BST satisfies:
1. Left subtree values < current node.
2. Right subtree values > current node.
3. Both left and right subtrees are BSTs.

Example:

        5
       / \
      3   7
     / \ / \
    2  4 6  8

Output:
True
"""



# Tree Node
# -------------------------

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# Validate BST
# -------------------------

def is_valid_bst(root):

    def validate(node, minimum, maximum):

        if node is None:
            return True

        if node.value <= minimum or node.value >= maximum:
            return False

        return (
            validate(node.left, minimum, node.value)
            and
            validate(node.right, node.value, maximum)
        )

    return validate(root, float("-inf"), float("inf"))


# Test Case 1 (Valid BST)
# -------------------------

root1 = TreeNode(5)

root1.left = TreeNode(3)
root1.right = TreeNode(7)

root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)

root1.right.left = TreeNode(6)
root1.right.right = TreeNode(8)

print("Tree 1 is BST:", is_valid_bst(root1))

print()

# Test Case 2 (Invalid BST)
# -------------------------

root2 = TreeNode(5)

root2.left = TreeNode(3)
root2.right = TreeNode(7)

root2.left.left = TreeNode(2)
root2.left.right = TreeNode(6)   # Invalid

print("Tree 2 is BST:", is_valid_bst(root2))