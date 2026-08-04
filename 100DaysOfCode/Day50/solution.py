"""
Day 50 - LRU Cache

Problem:
Design a data structure that follows the
Least Recently Used (LRU) Cache policy.

Operations:
1. get(key) -> Return value if key exists, else -1.
2. put(key, value) -> Insert or update key.
3. If capacity is exceeded, remove the Least Recently Used item.

Time Complexity:
get()  -> O(1)
put()  -> O(1)
"""

# Doubly Linked List Node
# -------------------------

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# LRU Cache
# -------------------------

class LRUCache:

    def __init__(self, capacity):

        self.capacity = capacity
        self.cache = {}

        # Dummy Head and Tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

   
    # Remove Node
    # -------------------------
    def remove(self, node):

        previous = node.prev
        nxt = node.next

        previous.next = nxt
        nxt.prev = previous

   
    # Insert Node at Front
    # -------------------------
    def insert(self, node):

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

 
    # Get Value
    # -------------------------
    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to front (Recently Used)
        self.remove(node)
        self.insert(node)

        return node.value

    
    # Put Value
    # -------------------------
    def put(self, key, value):

        if key in self.cache:

            self.remove(self.cache[key])

        node = Node(key, value)

        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:

            # Remove Least Recently Used
            lru = self.tail.prev

            self.remove(lru)

            del self.cache[lru.key]



# Test
# -------------------------

cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))      # 10

cache.put(3, 30)         # Removes key 2

print(cache.get(2))      # -1

cache.put(4, 40)         # Removes key 1

print(cache.get(1))      # -1
print(cache.get(3))      # 30
print(cache.get(4))      # 40