# DAY 10 - DSA Practice (Two Pointer + Sliding Window)

# Two Sum (Two Pointers, sorted array)
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []


# Reverse Array (Two Pointers)
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


# Maximum Sum Subarray of Size K (Sliding Window)
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


#  Longest Substring Without Repeating Characters
def longest_unique_substring(s):
    char_index = {}
    start = 0
    max_len = 0

    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_len = max(max_len, end - start + 1)

    return max_len


# Testing
arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 10
k = 3
text = "abcabcbb"

print("Two Sum Indices:", two_sum_sorted(arr, target))
print("Reverse Array:", reverse_array(arr))
print("Max Sum Subarray of size 3:", max_sum_subarray([2, 1, 5, 1, 3, 2], k))
print("Longest Unique Substring:", longest_unique_substring(text))