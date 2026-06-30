# Day 23 - Counting Sort

def counting_sort(arr):

    if not arr:
        return arr

    max_value = max(arr)

    count = [0] * (max_value + 1)

    # Count frequency
    for num in arr:
        count[num] += 1

    sorted_array = []

    # Build sorted array
    for i in range(len(count)):
        while count[i] > 0:
            sorted_array.append(i)
            count[i] -= 1

    return sorted_array


numbers = [4, 2, 2, 8, 3, 3, 1]

print("Original Array:")
print(numbers)

print("\nSorted Array:")
print(counting_sort(numbers))