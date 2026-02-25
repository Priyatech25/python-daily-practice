# DAY 2 - DSA Practice (Searching)

#  Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search (Array must be sorted)
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


#  Count Occurrences
def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count


# Testing
arr = [5, 10, 15, 20, 25, 30]
target = 20

print("Array:", arr)
print("Linear Search Index:", linear_search(arr, target))
print("Binary Search Index:", binary_search(arr, target))
print("Count Occurrences:", count_occurrences(arr, target))