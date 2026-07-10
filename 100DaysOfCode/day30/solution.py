"""
Day 31 - Two Sum II (Input Array Is Sorted)

Problem:
Given a sorted array of integers and a target value,
return the indices (1-based) of the two numbers such that they add up to the target.

Example:
Input:
numbers = [2, 7, 11, 15]
target = 9

Output:
[1, 2]
"""

def two_sum(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left < right:

        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return []


# HackerRank pblm

numbers = [2, 7, 11, 15]
target = 9

print("Array :", numbers)
print("Target:", target)
print("Answer:", two_sum(numbers, target))

print()

numbers = [2, 3, 4]
target = 6

print("Array :", numbers)
print("Target:", target)
print("Answer:", two_sum(numbers, target))

print()

numbers = [-1, 0]
target = -1

print("Array :", numbers)
print("Target:", target)
print("Answer:", two_sum(numbers, target))