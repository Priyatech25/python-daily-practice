"""
Day 48 - Binary Tree Level Order Traversal

Problem:
Given the root of a binary tree,
return the level order traversal of its nodes'
values (from left to right, level by level).

Example:

        3
       / \
      9   20
         /  \
        15   7

Output:
[[3], [9,20], [15,7]]
"""

from collections import deque



# Tree Node
# -------------------------

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# Level Order Traversal
# -------------------------

def level_order(root):

    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:

        level = []
        level_size = len(queue)

        for _ in range(level_size):

            node = queue.popleft()

            level.append(node.value)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

    return result



# Create Tree
# -------------------------

root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode

# Test
# -------------------------

print("Level Order Traversal:")
print(level_order(root))