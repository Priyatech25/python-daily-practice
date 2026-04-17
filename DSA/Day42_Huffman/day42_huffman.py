# DAY 42 - Huffman Decoding

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def decode_huffman(root, s):
    result = ""
    current = root

    for bit in s:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        # If leaf node
        if current.left is None and current.right is None:
            result += current.data
            current = root

    return result


# Example Huffman Tree
root = Node('*')
root.left = Node('A')
root.right = Node('*')
root.right.left = Node('B')
root.right.right = Node('C')

# Encoded string
encoded = "0110110"

print("Decoded String:", decode_huffman(root, encoded))