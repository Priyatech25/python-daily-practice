# DAY 16 - DSA Practice (Heap)

import heapq

# Create empty heap
heap = []

# Insert elements
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 1)

print("Heap Elements:", heap)

# Get smallest element
print("Smallest Element:", heap[0])

# Remove smallest element
removed = heapq.heappop(heap)
print("Removed Element:", removed)

print("Heap After Removal:", heap)