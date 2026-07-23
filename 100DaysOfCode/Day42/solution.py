"""
Day 42 - Merge Intervals

Problem:
Given an array of intervals where intervals[i] = [start, end],
merge all overlapping intervals.

Example:

Input:
[[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]
"""


def merge_intervals(intervals):

    if not intervals:
        return []

    # Sort intervals based on starting value
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:

        last = merged[-1]

        # Overlapping intervals
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])

        else:
            merged.append(current)

    return merged


# Test Cases
# -------------------------

intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print("Input :", intervals1)
print("Output:", merge_intervals(intervals1))

print()

intervals2 = [[1, 4], [4, 5]]
print("Input :", intervals2)
print("Output:", merge_intervals(intervals2))

print()

intervals3 = [[1, 5], [2, 3]]
print("Input :", intervals3)
print("Output:", merge_intervals(intervals3))

print()

intervals4 = [[6, 8], [1, 9], [2, 4], [4, 7]]
print("Input :", intervals4)
print("Output:", merge_intervals(intervals4))