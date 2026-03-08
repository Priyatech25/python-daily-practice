# DAY 13 - DSA Practice (Binary Search Tree)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Insert node in BST
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


# Search in BST
def search(root, key):
    if root is None or root.key == key:
        return root

    if key < root.key:
        return search(root.left, key)

    return search(root.right, key)


# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Creating BST
root = None
values = [50, 30, 20, 40, 70, 60, 80]

for v in values:
    root = insert(root, v)

print("Inorder Traversal (Sorted):")
inorder(root)

# Searching element
key = 40
result = search(root, key)

if result:
    print("\nElement found:", result.key)
else:
    print("\nElement not found")