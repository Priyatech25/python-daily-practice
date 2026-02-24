# DAY 1 - DSA Practice (Arrays)

#  Reverse an Array
def reverse_array(arr):
    return arr[::-1]


#  Find Second Largest Element
def second_largest(arr):
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second


# Check if Array is Sorted
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


# Testing
arr = [10, 20, 5, 8, 30]

print("Original:", arr)
print("Reversed:", reverse_array(arr))
print("Second Largest:", second_largest(arr))
print("Is Sorted:", is_sorted(arr))