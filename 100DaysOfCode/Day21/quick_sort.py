# Day 22 - Quick Sort

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original Array:")
print(numbers)

sorted_array = quick_sort(numbers)

print("\nSorted Array:")
print(sorted_array)