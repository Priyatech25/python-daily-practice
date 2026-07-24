"""
Day 43 - Insert Interval

Problem:
You are given a list of non-overlapping intervals sorted by their start times.

Insert a new interval into the list and merge if necessary.

Example:

Input:
intervals = [[1,3],[6,9]]
newInterval = [2,5]

Output:
[[1,5],[6,9]]
"""


def insert_interval(intervals, new_interval):

    result = []
    i = 0
    n = len(intervals)

    # Add intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


# Test Cases
# -------------------------

intervals1 = [[1, 3], [6, 9]]
new_interval1 = [2, 5]

print("Input:")
print("Intervals:", intervals1)
print("New Interval:", new_interval1)
print("Output:", insert_interval(intervals1, new_interval1))

print()

intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval2 = [4, 8]

print("Input:")
print("Intervals:", intervals2)
print("New Interval:", new_interval2)
print("Output:", insert_interval(intervals2, new_interval2))

print()

intervals3 = []
new_interval3 = [5, 7]

print("Input:")
print("Intervals:", intervals3)
print("New Interval:", new_interval3)
print("Output:", insert_interval(intervals3, new_interval3))