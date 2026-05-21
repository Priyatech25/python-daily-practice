# Day 14 - Heap Basics

import heapq

# Min Heap
numbers = [40, 10, 30, 50, 20]

heapq.heapify(numbers)

print("Min Heap:")
print(numbers)

# Push element
heapq.heappush(numbers, 5)

print("\nAfter Push:")
print(numbers)

# Pop smallest element
smallest = heapq.heappop(numbers)

print("\nRemoved Smallest Element:")
print(smallest)

print("Heap After Pop:")
print(numbers)

# Max Heap using negative values
max_heap = []

values = [40, 10, 30, 50, 20]

for value in values:
    heapq.heappush(max_heap, -value)

print("\nMax Heap:")

while max_heap:
    print(-heapq.heappop(max_heap), end=" ")