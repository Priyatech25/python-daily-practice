# Day 30 - LRU Cache

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    # Get value by key
    def get(self, key):

        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    # Insert or update key
    def put(self, key, value):

        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            removed = self.cache.popitem(last=False)
            print("Removed:", removed)


cache = LRUCache(3)

cache.put(1, "Python")
cache.put(2, "Java")
cache.put(3, "C++")

print("Cache:", cache.cache)

print("\nAccess Key 2:", cache.get(2))

cache.put(4, "JavaScript")

print("\nFinal Cache:")
print(cache.cache)