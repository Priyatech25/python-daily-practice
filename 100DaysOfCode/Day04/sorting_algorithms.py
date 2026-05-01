# Day 4 - Sorting Algorithms

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Selection Sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


numbers1 = [64, 34, 25, 12, 22, 11, 90]
numbers2 = [64, 34, 25, 12, 22, 11, 90]

print("Original Array:", numbers1)
print("Bubble Sort:", bubble_sort(numbers1))
print("Selection Sort:", selection_sort(numbers2))