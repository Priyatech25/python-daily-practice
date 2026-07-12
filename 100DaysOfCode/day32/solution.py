"""
Day 33 - Move Zeroes

Problem:
Move all 0's to the end of the array while maintaining
the relative order of non-zero elements.

Example:

Input:
[0,1,0,3,12]

Output:
[1,3,12,0,0]
"""


def move_zeroes(nums):

    position = 0

    # Move non-zero elements forward
    for i in range(len(nums)):

        if nums[i] != 0:
            nums[position], nums[i] = nums[i], nums[position]
            position += 1

    return nums



soln
# -------------------------

nums1 = [0, 1, 0, 3, 12]
print("Original:", nums1)
print("Result  :", move_zeroes(nums1))

print()

nums2 = [0, 0, 1]
print("Original:", nums2)
print("Result  :", move_zeroes(nums2))

print()

nums3 = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
print("Original:", nums3)
print("Result  :", move_zeroes(nums3))