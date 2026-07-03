# Day 25 - Priority Queue using Heap

import heapq

# Create an empty priority queue
priority_queue = []

# Insert elements
heapq.heappush(priority_queue, 30)
heapq.heappush(priority_queue, 10)
heapq.heappush(priority_queue, 20)
heapq.heappush(priority_queue, 5)
heapq.heappush(priority_queue, 15)

print("Priority Queue:")
print(priority_queue)

# Peek highest priority (smallest element)
print("\nTop Priority:", priority_queue[0])

# Remove elements by priority
print("\nProcessing Elements:")

while priority_queue:
    element = heapq.heappop(priority_queue)
    print(element)