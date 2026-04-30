# Day 3 - Searching Algorithms

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

print("Array:", numbers)
print("Target:", target)

linear_result = linear_search(numbers, target)
binary_result = binary_search(numbers, target)

print("Linear Search Result:", linear_result)
print("Binary Search Result:", binary_result)