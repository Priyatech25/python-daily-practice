# DAY 24 - DSA Practice (Array Manipulation)

def array_manipulation(n, queries):
    arr = [0] * (n + 1)

    # Apply operations
    for l, r, val in queries:
        arr[l - 1] += val
        if r < n:
            arr[r] -= val

    # Prefix sum to get final values
    max_value = 0
    current = 0

    for i in range(n):
        current += arr[i]
        max_value = max(max_value, current)

    return max_value


# Testing
n = 5
queries = [
    (1, 3, 100),
    (2, 5, 100),
    (3, 4, 100)
]

print("Maximum value after operations:", array_manipulation(n, queries))