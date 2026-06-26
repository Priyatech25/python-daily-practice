# Day 19 - Binary Search

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


numbers = [5, 12, 18, 25, 32, 41, 56, 63, 78, 91]
target = 41

index = binary_search(numbers, target)

print("Array:", numbers)
print("Target:", target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")