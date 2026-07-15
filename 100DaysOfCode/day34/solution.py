"""
Day 34 - Contains Duplicate

Problem:
Given an integer array nums,
return True if any value appears at least twice.
Return False if every element is distinct.

Example:

Input:
nums = [1,2,3,1]

Output:
True
"""


def contains_duplicate(nums):

    seen = set()

    for num in nums:

        if num in seen:
            return True

        seen.add(num)

    return False


# soln
# -------------------------

nums1 = [1, 2, 3, 1]
print("Input :", nums1)
print("Output:", contains_duplicate(nums1))

print()

nums2 = [1, 2, 3, 4]
print("Input :", nums2)
print("Output:", contains_duplicate(nums2))

print()

nums3 = [5, 5, 5, 5]
print("Input :", nums3)
print("Output:", contains_duplicate(nums3))

print()

nums4 = [10, 20, 30, 40, 50]
print("Input :", nums4)
print("Output:", contains_duplicate(nums4))