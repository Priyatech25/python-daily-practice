# DAY 41 - Heap (Kth Largest Element)

import heapq

def find_kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


# Test
nums = [3, 2, 1, 5, 6, 4]
k = 2

print("Kth Largest Element:", find_kth_largest(nums, k))