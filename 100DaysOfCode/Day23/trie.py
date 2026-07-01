# Day 24 - Trie (Prefix Tree)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    # Search a complete word
    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end

    # Check if prefix exists
    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True


trie = Trie()

words = ["apple", "app", "bat", "ball"]

for word in words:
    trie.insert(word)

print("Search 'apple':", trie.search("apple"))
print("Search 'bat':", trie.search("bat"))
print("Search 'cat':", trie.search("cat"))

print("Starts with 'ap':", trie.starts_with("ap"))
print("Starts with 'ba':", trie.starts_with("ba"))
print("Starts with 'ca':", trie.starts_with("ca"))