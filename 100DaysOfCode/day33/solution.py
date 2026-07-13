"""
Day 34 - Product of Array Except Self

Problem:
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums
except nums[i].

Do not use division.

Example:

Input:
nums = [1,2,3,4]

Output:
[24,12,8,6]
"""


def product_except_self(nums):

    n = len(nums)

    answer = [1] * n

    # Calculate prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Calculate suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


# soln
# -------------------------

nums1 = [1, 2, 3, 4]
print("Input :", nums1)
print("Output:", product_except_self(nums1))

print()

nums2 = [-1, 1, 0, -3, 3]
print("Input :", nums2)
print("Output:", product_except_self(nums2))

print()

nums3 = [2, 5, 10]
print("Input :", nums3)
print("Output:", product_except_self(nums3))